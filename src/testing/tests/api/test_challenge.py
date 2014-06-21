import pytest

from battlehack.api.views import challenge_detail
from testing.factories.factory_core import ChallengeFactory


@pytest.mark.django_db
class TestChallengeDetail:

    def test_get(self, rf):
        challenge = ChallengeFactory.create()
        request = rf.get('/', {'format': 'json'})
        response = challenge_detail(request, pk=challenge.pk)
        assert response.data['id'] == challenge.id
