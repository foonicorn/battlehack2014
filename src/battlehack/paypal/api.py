import paypalrestsdk

from django.core.urlresolvers import reverse

from . import models


def payment_start(payment, base_url):
    if not payment.status == models.STATUS_INITIATED:
        raise Exception('Wrong payment status')

    base_url = base_url.strip('/')
    return_url = base_url + reverse('paypal:success', kwargs={'uuid': payment.attendee.uuid})

    paypal_payment = paypalrestsdk.Payment({
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
                'total': '{0:.2f}'.format(payment.attendee.challenge.amount),
                'currency': 'EUR'
            },
            'description': payment.attendee.challenge.description
        }]
    })

    result = paypal_payment.create()
    if not result:
        payment.status = models.STATUS_FAILED
        payment.save()
        raise Exception(paypal_payment.error)

    payment.pid = paypal_payment.id
    payment.status = models.STATUS_CREATED
    payment.save()
    return paypal_payment


def execute_payment(payment, payer_id):
    paypal_payment = paypalrestsdk.Payment.find(payment.pid)
    result = paypal_payment.execute({'payer_id': payer_id})
    if not result:
        payment.status = models.STATUS_FAILED
        payment.save()
        raise Exception(paypal_payment.error)

    payment.status = models.STATUS_EXECUTED
    payment.save()
    return paypal_payment


def get_approval_url(paypal_payment):
    for link in paypal_payment.links:
        if link.method == 'REDIRECT':
            return link.href
    raise Exception('No approval url found')
