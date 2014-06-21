from battlehack.paypal import api
from testing.factories.factory_core import ChallengeFactory


def test_payment_create_owner(db):
    challenge = ChallengeFactory.create()
    #api.payment_owner_create(challenge)
