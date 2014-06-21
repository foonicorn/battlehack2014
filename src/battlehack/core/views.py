from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView

from . import models

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
