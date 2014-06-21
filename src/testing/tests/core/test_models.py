from testing.factories.factory_core import ChallengeFactory


def test_challenge(db):
    challenge = ChallengeFactory.create()
    assert challenge.owner
    assert challenge.charity
