from testing.factories.factory_core import ChallengeFactory, OwnerFactory, RivalFactory


def test_challenge(db):
    challenge = ChallengeFactory.create()
    assert challenge.charity


def test_attendee(db):
    challenge = ChallengeFactory.create()
    owner = OwnerFactory(challenge=challenge)
    rival = RivalFactory(challenge=challenge)
    assert owner.challenge
    assert owner.uuid
    assert owner.opponent == rival
    assert rival.opponent == owner
