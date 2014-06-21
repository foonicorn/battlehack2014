import pytest

from django.core.urlresolvers import reverse
from mock import patch

from battlehack.paypal import views
from testing.factories.factory_core import ChallengeFactory
from testing.factories.factory_request import RequestFactory
from testing.factories.factory_user import UserFactory


@pytest.mark.django_db
class TestPaypalStart:

    @patch('battlehack.paypal.views.PaypalStart.get_redirect_url')
    def test(self, mock):
        mock.return_value = '/foo/'
        challenge = ChallengeFactory.create()
        url = reverse('paypal:start', kwargs={'challenge_pk': challenge.pk})
        assert url.startswith('/paypal/start/')

        user = UserFactory.create()
        request = RequestFactory.get('/', user=user)
        response = views.start(request, challenge_pk=challenge.pk)
        assert response.status_code == 302
        assert response['Location'] == '/foo/'
