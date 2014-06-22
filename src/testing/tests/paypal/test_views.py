import pytest

from django.core.urlresolvers import reverse
from mock import patch, Mock

from battlehack.paypal import views
from testing.factories.factory_core import ChallengeFactory
from testing.factories.factory_request import RequestFactory


def paypal_start_payment_factory():
    link_mock = Mock()
    link_mock.method = 'REDIRECT'
    link_mock.href = '/paypal/'
    mock = Mock()
    mock.links = [link_mock]
    return mock


@pytest.mark.django_db
class TestPaypalStart:

    def test_url(self):
        url = reverse('paypal:start', kwargs={'spk': '1.X'})
        assert url == '/paypal/start/1.X/'

    @patch('battlehack.paypal.views.PaypalStart.start_payment')
    def test_get(self, mock):
        mock.return_value = paypal_start_payment_factory()
        challenge = ChallengeFactory.create()
        payment = challenge.rival_payment
        request = RequestFactory.get('/')
        response = views.start(request, spk=payment.spk)
        mock.assert_called_with(payment)
        assert response.status_code == 302
        assert response['Location'] == '/paypal/'


@pytest.mark.django_db
class TestPaypalSuccess:

    def test_url(self):
        url = reverse('paypal:success', kwargs={'spk': '1.X'})
        assert url

    @patch('battlehack.paypal.views.PaypalSuccess.execute_payment')
    def test_get(self, mock):
        challenge = ChallengeFactory.create()
        payment = challenge.rival_payment
        request = RequestFactory.get('/', data={'PayerID': 'ABC'})
        response = views.success(request, spk=payment.spk)
        assert response.status_code == 302
        assert response['Location'] == '/challenges/{0}/'.format(payment.challenge.spk)
