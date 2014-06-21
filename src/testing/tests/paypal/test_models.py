from testing.factories.factory_paypal import PaymentFactory


def test_payment(db):
    payment = PaymentFactory.create()
    assert payment.user
    assert payment.challenge
