from battlehack.paypal.models import Payment, TYPE_OWNER, TYPE_RIVAL
from testing.factories.factory_core import ChallengeFactory, RivalFactory


def test_challenge(db):
    challenge = ChallengeFactory.create()
    assert challenge.owner
    assert challenge.charity
    assert Payment.objects.get(challenge=challenge, type=TYPE_OWNER)
    assert Payment.objects.get(challenge=challenge, type=TYPE_RIVAL)


def test_rival(db):
    rival = RivalFactory.create()
    assert rival.challenge
