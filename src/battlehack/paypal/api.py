import paypalrestsdk

from django.core.urlresolvers import reverse

from . import models
from battlehack.core.models import Attendee


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


def finish(owner, rival):
    results = []
    if owner.status == rival.status:
        results.append(capture_payment(owner.payment))
        results.append(capture_payment(rival.payment))
    elif owner.status == Attendee.STATUS_LOOSE:
        results.append(capture_payment(owner.payment))
        results.append(void_payment(rival.payment))
    elif rival.status == Attendee.STATUS_LOOSE:
        results.append(capture_payment(rival.payment))
        results.append(void_payment(owner.payment))
    return all(results)


def capture_payment(payment):
    paypal_payment = paypalrestsdk.Payment.find(payment.pid)
    authorization = get_authorization(paypal_payment)
    result = authorization.capture({
        'is_final_capture': True,
        'amount': {
            'currency': authorization.amount.currency,
            'total': authorization.amount.total,
        },
    })
    success = result.success()
    if success:
        payment.status = models.STATUS_CAPTURED
        payment.save()
    return success


def void_payment(payment):
    paypal_payment = paypalrestsdk.Payment.find(payment.pid)
    authorization = get_authorization(paypal_payment)
    success = authorization.void()
    if success:
        payment.status = models.STATUS_VOIDED
        payment.save()
    return success


def get_approval_url(paypal_payment):
    for link in paypal_payment.links:
        if link.method == 'REDIRECT':
            return link.href
    raise Exception('No approval url found')


def get_authorization(paypal_payment):
    for transaction in paypal_payment.transactions:
        for resource in transaction.related_resources:
            if resource.authorization:
                authorization_id = resource.authorization.id
                return paypalrestsdk.Authorization.find(authorization_id)
    raise Exception('No authorization found')
