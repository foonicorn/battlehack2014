from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from . import api
from .models import Payment
from battlehack.core.models import Challenge


class PaypalStart(RedirectView):
    permanent = False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaypalStart, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, challenge_pk):
        challenge = get_object_or_404(Challenge, pk=challenge_pk)
        base_url = self.request.build_absolute_uri('/')
        payment = api.payment_owner_create(challenge, base_url)
        redirect_url = api.get_redirect_url(payment)
        return redirect_url

start = PaypalStart.as_view()


class PaypalSuccess(RedirectView):
    permanent = False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaypalSuccess, self).dispatch(*args, **kwargs)

    def get(self, request, payment_pk, *args, **kwargs):
        payer_id = self.request.GET.get('PayerID')
        if not payer_id:
            raise Http404('No PayerID')
        self.payment = get_object_or_404(Payment, pk=payment_pk)
        self.execute_payment(self.payment, payer_id)
        return super(PaypalSuccess, self).get(request, *args, **kwargs)

    def execute_payment(self, payment, payer_id):
        api.execute_payment(payment, payer_id)

    def get_redirect_url(self):
        challenge_pk = self.payment.challenge_id
        return '/foo/'
        #return reverse('core:detail', kwargs={'challenge_pk': challenge_pk})

success = PaypalSuccess.as_view()
