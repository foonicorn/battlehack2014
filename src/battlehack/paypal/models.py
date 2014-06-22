from django.db import models
from django.utils.translation import ugettext_lazy as _

from battlehack.utils.signing import sign


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
    type = models.CharField(_('type'), max_length=20, choices=TYPE_CHOICES)
    pid = models.CharField(_('payment id'), max_length=100, blank=True)
    status = models.CharField(
        _('status'), max_length=20,
        choices=STATUS_CHOICES, default=STATUS_INITIATED)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')
        unique_together = ('challenge', 'type')

    def __unicode__(self):
        return u'{0} / {1}'.format(self.type, self.pid)

    @property
    def spk(self):
        return sign(self.pk)
