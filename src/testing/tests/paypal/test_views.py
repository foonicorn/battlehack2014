import pytest

from django.core.urlresolvers import reverse
from mock import patch

from battlehack.paypal import views
from testing.factories.factory_core import ChallengeFactory
from testing.factories.factory_paypal import PaymentFactory
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


@pytest.mark.django_db
class TestPaypalSuccess:

    def test_url(self):
        url = reverse('paypal:success', kwargs={'payment_pk': 1})
        assert url

    @patch('battlehack.paypal.views.PaypalSuccess.execute_payment')
    def test_get(self, mock):
        payment = PaymentFactory.create()
        request = RequestFactory.get('/', user=payment.user, data={'PayerID': 'ABC'})
        response = views.success(request, payment_pk=payment.pk)
        assert response.status_code == 302
        assert response['Location'] == '/challenges/{0}/'.format(payment.challenge.pk)
