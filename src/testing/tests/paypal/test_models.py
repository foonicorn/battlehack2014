from testing.factories.factory_core import ChallengeFactory


def test_payment(db):
    challenge = ChallengeFactory.create()
    assert challenge.owner_payment
    assert challenge.rival_payment
