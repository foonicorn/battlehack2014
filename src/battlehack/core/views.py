from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, View
from django.views.generic.detail import SingleObjectMixin

from . import models, forms


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
        return qs.filter(attendee__user=self.request.user)

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
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        uuid = self.object.owner.uuid
        return reverse('paypal:start', kwargs={'uuid': uuid})

challenge_create = ChallengeCreate.as_view()


class ChallengeDetail(DetailView):
    model = models.Attendee
    template_name = 'core/challenge_detail.html'
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'

    def get_context_data(self, **kwargs):
        context = super(ChallengeDetail, self).get_context_data(**kwargs)
        context['challenge'] = self.object.challenge
        return context

challenge_detail = ChallengeDetail.as_view()


class ChallengeUpdate(SingleObjectMixin, View):
    model = models.Challenge

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ChallengeDetail, self).dispatch(*args, **kwargs)

    def post(self, request, pk, type, *args, **kwargs):
        return super(ChallengeUpdate, self).post(request, *args, **kwargs)
