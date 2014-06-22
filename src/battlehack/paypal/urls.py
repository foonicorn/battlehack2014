from django.conf.urls import patterns, url


urlpatterns = patterns(
    'battlehack.paypal.views',
    url('^start/(?P<payment_pk>\d+)/$', 'start', name='start'),
    url('^success/(?P<payment_pk>\d+)/$', 'success', name='success'),
)
