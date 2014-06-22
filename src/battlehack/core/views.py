from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView

from . import models, forms
from .mail import send_rival_email
from battlehack.paypal import api


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

    def get_context_data(self, **kwargs):
        context = super(ChallengeList, self).get_context_data(**kwargs)
        context['owner_sum'] = models.Attendee.objects.filter(
            user=self.request.user, status=models.Attendee.STATUS_WIN).aggregate(
            owner_sum=Sum('challenge__amount'))['owner_sum'] or 0
        context['rivals_sum'] = models.Attendee.objects.filter(
            user=self.request.user, status=models.Attendee.STATUS_LOOSE).aggregate(
            rivals_sum=Sum('challenge__amount'))['rivals_sum'] or 0
        context['total_sum'] = context['rivals_sum'] + context['owner_sum']
        return context

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
        self.send_email()
        return HttpResponseRedirect(self.get_success_url())

    def send_email(self):
        path = reverse('core:challenge_detail', kwargs={'uuid': self.object.rival.uuid})
        url = self.request.build_absolute_uri(path)
        send_rival_email(self.object.rival.email, url)

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


class AttendeeUpdate(UpdateView):
    model = models.Attendee
    slug_field = 'uuid'
    slug_url_kwarg = 'uuid'
    form_class = forms.AttendeeUpdateForm
    template_name = 'core/attendee_update.html'

    def form_valid(self, form):
        response = super(AttendeeUpdate, self).form_valid(form)
        challenge = self.object.challenge
        if not challenge.pending:
            api.finish(challenge.owner, challenge.rival)
        return response

    def get_success_url(self):
        return reverse('core:challenge_detail', kwargs={'uuid': self.object.uuid})

attendee_update = AttendeeUpdate.as_view()


class RivalStart(ChallengeDetail):
    template_name = 'core/rival_start.html'

rival_start = RivalStart.as_view()
