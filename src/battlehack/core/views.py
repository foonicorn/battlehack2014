from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView

from . import models, forms
from battlehack.paypal.models import Payment, TYPE_OWNER


class IndexView(TemplateView):
    template_name = 'core/index.html'

index = IndexView.as_view()


class LoginView(TemplateView):
    template_name = 'core/login.html'

login = LoginView.as_view()


class LogoutView(TemplateView):
    template_name = 'core/logout.html'

    def get(self, *args, **kwargs):
        auth.logout(self.request)
        return super(LogoutView, self).get(*args, **kwargs)

logout = LogoutView.as_view()


class ChallengeList(ListView):
    model = models.Challenge
    template_name = 'core/challenge_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChallengeList, self).dispatch(*args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        qs = super(ChallengeList, self).get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)

challenge_list = ChallengeList.as_view()


class ChallengeCreate(CreateView):
    model = models.Challenge
    form_class = forms.ChallengeCreateForm
    template_name = 'core/challenge_create.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChallengeCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(owner=self.request.user)
        payment = Payment.objects.get(challenge=self.object, type=TYPE_OWNER)
        return HttpResponseRedirect(self.get_success_url(payment))

    def get_success_url(self, payment):
        return reverse('paypal:start', kwargs={'payment_pk': payment.pk})

challenge_create = ChallengeCreate.as_view()


class ChallengeDetail(DetailView):
    model = models.Challenge
    template_name = 'core/challenge_detail.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChallengeDetail, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super(ChallengeDetail, self).get_queryset()
        return qs.filter(owner=self.request.user)

challenge_detail = ChallengeDetail.as_view()
