from django.conf.urls import patterns, url


urlpatterns = patterns(
    'battlehack.core.views',
    url('^$', 'index', name='index'),
    url(r'^login/$', 'login', name='login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^challenges/$', 'challenge_list', name='challenge_list'),
    url(r'^challenges/(?P<uuid>[\w\-]+)/$', 'challenge_detail', name='challenge_detail'),
    url(r'^create/$', 'challenge_create', name='challenge_create'),
    url(r'^update/(?P<uuid>[\w\-]+)/$', 'attendee_update', name='attendee_update'),
)
