from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^challenges/(?P<pk>[0-9]+)/$', views.challenge_detail),
)
