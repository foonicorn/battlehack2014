import pytest

from django.core.urlresolvers import reverse
from mock import patch, Mock

from battlehack.paypal import views
from testing.factories.factory_core import ChallengeFactory, OwnerFactory
from testing.factories.factory_request import RequestFactory
from testing.factories.factory_paypal import PaymentFactory


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
        url = reverse('paypal:start', kwargs={'uuid': '1'})
        assert url == '/paypal/start/1/'

    @patch('battlehack.paypal.views.PaypalStart.start_payment')
    def test_get(self, mock):
        mock.return_value = paypal_start_payment_factory()
        challenge = ChallengeFactory.create()
        owner = OwnerFactory(challenge=challenge)
        payment = PaymentFactory.create(attendee=owner)
        request = RequestFactory.get('/')
        response = views.start(request, uuid=payment.attendee.uuid)
        mock.assert_called_with(payment)
        assert response.status_code == 302
        assert response['Location'] == '/paypal/'


@pytest.mark.django_db
class TestPaypalSuccess:

    def test_url(self):
        url = reverse('paypal:success', kwargs={'uuid': '1'})
        assert url

    @patch('battlehack.paypal.views.PaypalSuccess.execute_payment')
    def test_get(self, mock):
        payment = PaymentFactory.create()
        request = RequestFactory.get('/', data={'PayerID': 'ABC'})
        response = views.success(request, uuid=payment.attendee.uuid)
        assert response.status_code == 302
        assert response['Location'] == '/challenges/{0}/'.format(payment.attendee.uuid)
