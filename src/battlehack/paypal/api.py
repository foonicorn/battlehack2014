import paypalrestsdk

from django.core.urlresolvers import reverse

from . import models


def payment_owner_create(challenge):
    if check_payment_exists(challenge, challenge.owner):
        raise Exception('Payment already exists')

    payment_request = paypalrestsdk.Payment({
        'intent': 'authorize',
        'redirect_urls': {
            'return_url': reverse('paypal:success'),
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
        raise Exception(payment_request.error)

    payment = models.Payment(
        pid=payment_request.id,
        challenge=challenge,
        user=challenge.owner,
        type=models.TYPE_OWNER,
        status=models.STATUS_CREATED
    )
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
