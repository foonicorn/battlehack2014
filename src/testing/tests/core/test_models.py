from testing.factories.factory_core import ChallengeFactory, AttendeeFactory


def test_challenge(db):
    challenge = ChallengeFactory.create()
    assert challenge.charity


def test_attendee(db):
    attendee = AttendeeFactory()
    assert attendee.challenge
    assert attendee.uuid
