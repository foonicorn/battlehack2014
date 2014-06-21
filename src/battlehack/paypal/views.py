from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from . import api
from battlehack.core import models


class PaypalStart(RedirectView):
    permanent = False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaypalStart, self).dispatch(*args, **kwargs)

    def get_redirect_url(self, challenge_pk):
        challenge = get_object_or_404(models.Challenge, pk=challenge_pk)
        payment = api.payment_owner_create(challenge)
        redirect_url = api.get_redirect_url(payment)
        return redirect_url

start = PaypalStart.as_view()


class PaypalSuccess(RedirectView):
    permanent = False

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PaypalSuccess, self).dispatch(*args, **kwargs)

success = PaypalSuccess.as_view()
