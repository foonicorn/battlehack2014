from django.contrib import auth
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'core/index.html'

index = IndexView.as_view()


class LogoutView(TemplateView):
    template_name = 'core/logout.html'

    def get(self, *args, **kwargs):
        auth.logout(self.request)
        return super(LogoutView, self).get(*args, **kwargs)

logout = LogoutView.as_view()
