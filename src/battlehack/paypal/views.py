from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, TemplateView

from . import api
from .models import Payment


class PaypalStart(RedirectView):
    permanent = False

    def get(self, request, uuid, *args, **kwargs):
        payment = get_object_or_404(Payment, attendee__uuid=uuid)
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

    def get(self, request, uuid, *args, **kwargs):
        payer_id = self.request.GET.get('PayerID')
        if not payer_id:
            raise Http404('No PayerID')
        self.payment = get_object_or_404(Payment, attendee__uuid=uuid)
        self.execute_payment(self.payment, payer_id)
        return super(PaypalSuccess, self).get(request, uuid, *args, **kwargs)

    def execute_payment(self, payment, payer_id):
        api.execute_payment(payment, payer_id)

    def get_redirect_url(self, uuid):
        return reverse('core:challenge_detail', kwargs={'uuid': uuid})

success = PaypalSuccess.as_view()


class PaypalCancel(TemplateView):
    template_name = 'core/paypal_cancel.html'

cancel = PaypalCancel.as_view()
