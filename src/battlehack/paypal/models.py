from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


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
    attendee = models.OneToOneField('core.Attendee', verbose_name=_('attendee'))
    pid = models.CharField(_('payment id'), max_length=100, blank=True)
    status = models.CharField(
        _('status'), max_length=20,
        choices=STATUS_CHOICES, default=STATUS_INITIATED)
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)

    class Meta:
        verbose_name = _('payment')
        verbose_name_plural = _('payments')

    def get_create_url(self):
        return reverse('paypal:start', kwargs={'uuid': self.attendee.uuid})

    def __unicode__(self):
        return u'{0} / {1}'.format(self.attendee, self.pid)
