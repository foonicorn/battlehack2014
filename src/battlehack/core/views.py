from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, View
from django.views.generic.detail import SingleObjectMixin

from . import models, forms
from battlehack.paypal.models import Payment, TYPE_OWNER
from battlehack.utils.signing import unsign


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
        return reverse('paypal:start', kwargs={'spk': payment.spk})

challenge_create = ChallengeCreate.as_view()


class ChallengeDetail(DetailView):
    model = models.Challenge
    template_name = 'core/challenge_detail.html'

    def get(self, request, spk, *args, **kwargs):
        self.kwargs['pk'] = unsign(spk)
        return super(ChallengeDetail, self).get(request, *args, **kwargs)

challenge_detail = ChallengeDetail.as_view()


class ChallengeUpdate(SingleObjectMixin, View):
    model = models.Challenge

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChallengeDetail, self).dispatch(*args, **kwargs)

    def post(self, request, pk, type, *args, **kwargs):
        return super(ChallengeUpdate, self).post(request, *args, **kwargs)
