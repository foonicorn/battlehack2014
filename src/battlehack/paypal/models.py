from django.db import models
from django.utils.translation import ugettext_lazy as _


TYPE_OWNER = 'owner'
TYPE_RIVAL = 'rival'
TYPE_CHOICES = (
    (TYPE_OWNER, _('owner')),
    (TYPE_RIVAL, _('rival')),
)

STATUS_INITIATED = 'initiated'
STATUS_CREATED = 'created'
STATUS_EXECUTED = 'executed'
STATUS_CAPTURED = 'captured'
STATUS_VOIDED = 'voided'
STATUS_FAILED = 'failed'
STATUS_CHOICES = (
    (STATUS_INITIATED, _('initiated')),
    (STATUS_CREATED, _('created')),
    (STATUS_EXECUTED, _('executed')),
    (STATUS_CAPTURED, _('captured')),
    (STATUS_VOIDED, _('voided')),
    (STATUS_FAILED, _('failed')),
)


class Payment(models.Model):
    challenge = models.ForeignKey('core.Challenge', verbose_name=_('challenge'))
    user = models.ForeignKey('auth.User', verbose_name=_('user'))
    type = models.CharField(_('type'), max_length=20, choices=TYPE_CHOICES)
    pid = models.CharField(_('payment id'), max_length=100, blank=True)
    status = models.CharField(
        _('status'), max_length=20, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def __unicode__(self):
        return self.pid
