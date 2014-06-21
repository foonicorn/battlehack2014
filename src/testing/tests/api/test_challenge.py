import pytest

from battlehack.api.views import challenge_detail, challenge_list
from testing.factories.factory_core import ChallengeFactory
from testing.factories.factory_request import RequestFactory
from testing.factories.factory_user import UserFactory


@pytest.mark.django_db
class TestChallengeDetail:

    def test_get_owner(self):
        challenge = ChallengeFactory.create()
        request = RequestFactory.get(
            '/', user=challenge.owner, data={'format': 'json'})
        response = challenge_detail(request, pk=challenge.pk)
        assert response.data['id'] == challenge.pk

    def test_get_anon(self):
        challenge = ChallengeFactory.create()
        request = RequestFactory.get('/', data={'format': 'json'})
        response = challenge_detail(request, pk=challenge.pk)
        assert response.status_code == 403


@pytest.mark.django_db
class TestChallengeList:

    def test_get_owner(self):
        challenge = ChallengeFactory.create()
        request = RequestFactory.get(
            '/', user=challenge.owner, data={'format': 'json'})
        response = challenge_list(request)
        assert len(response.data) == 1
        assert response.data[0]['id'] == challenge.pk

    def test_get_anon(self):
        ChallengeFactory.create()
        request = RequestFactory.get('/', data={'format': 'json'})
        response = challenge_list(request)
        assert response.status_code == 403

    def test_get_other(self):
        ChallengeFactory.create()
        user = UserFactory.create()
        request = RequestFactory.get('/', user=user, data={'format': 'json'})
        response = challenge_list(request)
        assert len(response.data) == 0

    def test_get_empty(self):
        user = UserFactory.create()
        request = RequestFactory.get('/', user=user, data={'format': 'json'})
        response = challenge_list(request)
        assert response.status_code == 200
        assert len(response.data) == 0
