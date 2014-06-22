from django.conf.urls import patterns, url


urlpatterns = patterns(
    'battlehack.paypal.views',
    url('^start/(?P<uuid>[\w\-]+)/$', 'start', name='start'),
    url('^success/(?P<uuid>[\w\-]+)/$', 'success', name='success'),
)
