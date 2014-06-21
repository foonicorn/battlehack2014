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


TYPE_OWNER = 'owner'
TYPE_RIVAL = 'rival'
TYPE_CHOICES = (
    (TYPE_OWNER, _('owner')),
    (TYPE_RIVAL, _('rival')),
)

STATUS_CREATED = 'created'
STATUS_EXECUTED = 'executed'
STATUS_CAPTURED = 'captured'
STATUS_VOIDED = 'voided'
STATUS_FAILED = 'failed'
STATUS_CHOICES = (
    (STATUS_CREATED, _('created')),
    (STATUS_EXECUTED, _('executed')),
    (STATUS_CAPTURED, _('captured')),
    (STATUS_VOIDED, _('voided')),
    (STATUS_FAILED, _('failed')),
)

class Payment(models.Model):
    challenge = models.ForeignKey(Challenge, verbose_name=_('challenge'))
    user = models.ForeignKey('auth.User', verbose_name=_('user'))
    type = models.CharField(_('type'), max_length=20, choices=TYPE_CHOICES)
    pid = models.CharField(_('payment id'), max_length=100)
    status = models.CharField(
        _('status'), max_length=20, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __unicode__(self):
        return self.pid
