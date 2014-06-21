from django.conf.urls import patterns, url


urlpatterns = patterns(
    'battlehack.api.views',
    url(r'^challenges/', 'challenge_list', name='challenge_list'),
    url(r'^challenges/(?P<pk>[0-9]+)/$', 'challenge_detail', name='challenge_list'),
)
