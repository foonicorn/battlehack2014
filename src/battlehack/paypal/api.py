import paypalrestsdk

from django.core.urlresolvers import reverse

from . import models


def payment_owner_create(challenge, base_url):
    if check_payment_exists(challenge, challenge.owner):
        raise Exception('Payment already exists')

    payment = models.Payment.objects.create(
        challenge=challenge,
        user=challenge.owner,
        type=models.TYPE_OWNER,
        status=models.STATUS_INITIATED
    )

    base_url = base_url.strip('/')
    return_url = base_url + reverse('paypal:success', kwargs={'payment_pk': payment.pk})

    payment_request = paypalrestsdk.Payment({
        'intent': 'authorize',
        'redirect_urls': {
            'return_url': return_url,
            'cancel_url': 'http://localhost:8000/paypal/cancel/',
        },
        'payer': {
            'payment_method': 'paypal',
        },
        'transactions': [{
            'amount': {
                'total': '{0:.2f}'.format(challenge.amount),
                'currency': 'EUR'
            },
            'description': challenge.description
        }]
    })

    result = payment_request.create()
    if not result:
        payment.status = models.STATUS_FAILED
        payment.save()
        raise Exception(payment_request.error)

    payment.pid = payment_request.id
    payment.status = models.STATUS_CREATED
    payment.save()
    return payment_request


def execute_payment(payment, payer_id):
    payment_request = paypalrestsdk.Payment.find(payment.pid)
    result = payment_request.execute({'payer_id': payer_id})
    if not result:
        payment.status = models.STATUS_FAILED
        payment.save()
        raise Exception(payment_request.error)

    payment.status = models.STATUS_EXECUTED
    payment.save()
    return payment_request


def check_payment_exists(challenge, user):
    qs = models.Payment.objects.filter(challenge=challenge, user=user)
    if qs.exists():
        return True


def get_redirect_url(payment):
    for link in payment.links:
        if link.method == 'REDIRECT':
            return link.href
    raise Exception('No redirect found')
