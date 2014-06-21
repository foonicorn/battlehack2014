from testing.factories.factory_core import ChallengeFactory, PaymentFactory


def test_challenge(db):
    challenge = ChallengeFactory.create()
    assert challenge.owner
    assert challenge.charity

def test_payment(db):
    payment = PaymentFactory.create()
    assert payment.user
    assert payment.challenge
