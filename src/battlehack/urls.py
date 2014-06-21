from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from battlehack.utils.views import GenericTemplateView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url('^api/', include('battlehack.api.urls', namespace='api')),
    url('^socialauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url('^', include('battlehack.core.urls', namespace='core')),
)


if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^test/((?P<template>[\w\-\/]+)/)?$', GenericTemplateView.as_view()),
        (
            r'^%s(?P<path>.*)$' % settings.MEDIA_URL.strip('/'),
            'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}
        ),
    )
