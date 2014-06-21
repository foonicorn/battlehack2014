import pytest

from django.core.urlresolvers import reverse

from battlehack.core import views
from testing.factories.factory_core import ChallengeFactory
from testing.factories.factory_request import RequestFactory
from testing.factories.factory_user import UserFactory


def test_index_view(rf):
    url = reverse('core:index')
    assert url
    request = rf.get(url)
    response = views.index(request)
    assert response.status_code == 200


def test_login_view():
    url = reverse('core:login')
    assert url
    request = RequestFactory.get(url)
    response = views.login(request)
    assert response.status_code == 200


def test_logout_view(db):
    url = reverse('core:logout')
    assert url
    user = UserFactory.create()
    request = RequestFactory.get(url, user=user)
    assert request.user.is_authenticated()
    response = views.logout(request)
    assert response.status_code == 200
    assert not request.user.is_authenticated()


@pytest.mark.django_db
class TestChallengeList:

    def test_get_owner(self):
        challenge = ChallengeFactory.create()
        request = RequestFactory.get('/', user=challenge.owner)
        response = views.challenge_list(request)
        assert response.status_code == 200
        assert challenge in response.context_data['object_list']

    def test_get_anon(self):
        request = RequestFactory.get('/')
        response = views.challenge_list(request)
        assert response.status_code == 302

    def test_get_other(self):
        challenge = ChallengeFactory.create()
        user = UserFactory.create()
        request = RequestFactory.get('/', user=user)
        response = views.challenge_list(request)
        assert response.status_code == 200
        assert challenge not in response.context_data['object_list']
