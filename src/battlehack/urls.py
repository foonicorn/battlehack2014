from django.conf import settings
from django.conf.urls import include, patterns, url
from django.contrib import admin

from battlehack.core.views import GenericTemplateView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url('^socialauth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
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