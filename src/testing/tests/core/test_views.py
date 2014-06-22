import pytest

from django.core.urlresolvers import reverse
from mock import patch

from battlehack.core import views, models
from testing.factories.factory_core import (
    ChallengeFactory, CharityFactory, OwnerFactory, RivalFactory)
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
        OwnerFactory.create(challenge=challenge)
        request = RequestFactory.get('/', user=challenge.owner.user)
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


@pytest.mark.django_db
class TestChallengeCreate:

    def test_anon(self):
        request = RequestFactory.get('/')
        response = views.challenge_create(request)
        assert response.status_code == 302
        assert response['Location'].startswith(reverse('core:login'))

    def test_get(self):
        user = UserFactory.create()
        request = RequestFactory.get('/', user=user)
        response = views.challenge_create(request)
        assert response.status_code == 200

    @patch('battlehack.core.views.send_rival_email')
    def test_post(self, mock):
        user = UserFactory.create()
        charity = CharityFactory.create()
        data = {
            'title': 'foo',
            'description': 'bar',
            'charity': charity.id,
            'amount': '1.50',
            'rival': 'rival@none.none',
        }
        request = RequestFactory.post('/', user=user, data=data)
        response = views.challenge_create(request)
        challenge = models.Challenge.objects.get(attendee__user=user)
        assert response.status_code == 302
        assert response['Location'] == '/paypal/start/{0}/'.format(challenge.owner.uuid)
        expected_rival_url = '/challenges/{0}/'.format(challenge.rival.uuid)
        assert mock.call_args[0][0] == 'rival@none.none'
        assert mock.call_args[0][1].endswith(expected_rival_url)


@pytest.mark.django_db
class TestChallengeDetail:

    def test_url(self):
        url = reverse('core:challenge_detail', kwargs={'uuid': '1'})
        assert url

    def test_get(self):
        challenge = ChallengeFactory.create()
        owner = OwnerFactory.create(challenge=challenge)
        request = RequestFactory.get('/')
        response = views.challenge_detail(request, uuid=owner.uuid)
        assert response.status_code == 200
        assert response.context_data['challenge'] == challenge


@pytest.mark.django_db
class TestAttendeeUpdate:

    def test_url(self):
        url = reverse('core:attendee_update', kwargs={'uuid': '1'})
        assert url

    def test_get(self):
        owner = OwnerFactory.create()
        request = RequestFactory.get('/')
        response = views.attendee_update(request, uuid=owner.uuid)
        assert response.status_code == 200
        assert response.context_data['form']

    def test_post(self):
        challenge = ChallengeFactory.create()
        owner = OwnerFactory.create(challenge=challenge)
        RivalFactory.create(challenge=challenge)
        data = {'status': 'win'}
        request = RequestFactory.post('/', data=data)
        response = views.attendee_update(request, uuid=owner.uuid)
        assert response.status_code == 302


@pytest.mark.django_db
class TestRivalStart:

    def test_url(self):
        url = reverse('core:rival_start', kwargs={'uuid': '1'})
        assert url

    def test_get(self):
        challenge = ChallengeFactory.create()
        rival = RivalFactory.create(challenge=challenge)
        request = RequestFactory.get('/')
        response = views.rival_start(request, uuid=rival.uuid)
        assert response.status_code == 200
        assert response.context_data['challenge'] == challenge
