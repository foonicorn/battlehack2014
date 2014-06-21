from django.db import models
from django.utils.translation import ugettext_lazy as _


class Charity(models.Model):
    name = models.CharField(_('name'), max_length=100)

    class Meta:
        verbose_name = _('charity')
        verbose_name_plural = _('charities')

    def __unicode__(self):
        return self.name


class Challenge(models.Model):
    owner = models.ForeignKey('auth.User', verbose_name=_('owner'))
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))
    charity = models.ForeignKey(Charity, verbose_name=_('charity'))
    amount = models.FloatField(_('amount'))
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('challenge')
        verbose_name_plural = _('challenges')

    def __unicode__(self):
        return self.title
