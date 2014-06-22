from django.conf.urls import patterns, url


urlpatterns = patterns(
    'battlehack.paypal.views',
    url('^start/(?P<spk>\d+\.[\w\-]+)/$', 'start', name='start'),
    url('^success/(?P<spk>\d+\.[\w\-]+)/$', 'success', name='success'),
)
