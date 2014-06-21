from django.conf.urls import patterns, url


urlpatterns = patterns(
    'battlehack.core.views',
    url('^$', 'index', name='index'),
    url(r'^logout/$', 'logout', name='logout'),
)
