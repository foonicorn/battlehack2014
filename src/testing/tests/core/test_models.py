from testing.factories.factory_core import ChallengeFactory, RivalFactory


def test_challenge(db):
    challenge = ChallengeFactory.create()
    assert challenge.owner
    assert challenge.charity


def test_rival(db):
    rival = RivalFactory.create()
    assert rival.challenge
