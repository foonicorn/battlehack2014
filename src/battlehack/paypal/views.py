from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView

from . import api
from .models import Payment
from battlehack.utils.signing import unsign


class PaypalStart(RedirectView):
    permanent = False

    def get(self, request, spk, *args, **kwargs):
        pk = unsign(spk)
        payment = get_object_or_404(Payment, pk=pk)
        paypal_payment = self.start_payment(payment)
        redirect_url = self.get_redirect_url(paypal_payment)
        return HttpResponseRedirect(redirect_url)

    def start_payment(self, payment):
        base_url = self.request.build_absolute_uri('/')
        return api.payment_start(payment, base_url)

    def get_redirect_url(self, paypal_payment):
        return api.get_approval_url(paypal_payment)


start = PaypalStart.as_view()


class PaypalSuccess(RedirectView):
    permanent = False

    def get(self, request, spk, *args, **kwargs):
        pk = unsign(spk)
        payer_id = self.request.GET.get('PayerID')
        if not payer_id:
            raise Http404('No PayerID')
        self.payment = get_object_or_404(Payment, pk=pk)
        self.execute_payment(self.payment, payer_id)
        return super(PaypalSuccess, self).get(request, *args, **kwargs)

    def execute_payment(self, payment, payer_id):
        api.execute_payment(payment, payer_id)

    def get_redirect_url(self):
        challenge_spk = self.payment.challenge.spk
        return reverse('core:challenge_detail', kwargs={'spk': challenge_spk})

success = PaypalSuccess.as_view()
