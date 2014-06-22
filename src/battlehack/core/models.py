from django.db import models
from django.utils.translation import ugettext_lazy as _

from battlehack.paypal.models import Payment, TYPE_OWNER, TYPE_RIVAL


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

    @property
    def owner_payment(self):
        return self.payment_set.get(type=TYPE_OWNER)

    @property
    def rival_payment(self):
        return self.payment_set.get(type=TYPE_RIVAL)

    def save(self, *args, **kwargs):
        create_payments = (self.id is None)
        result = super(Challenge, self).save(*args, **kwargs)
        if create_payments:
            Payment.objects.create(challenge=self, type=TYPE_OWNER)
            Payment.objects.create(challenge=self, type=TYPE_RIVAL)
        return result


class Rival(models.Model):
    challenge = models.ForeignKey(Challenge, verbose_name=_('challenge'))
    email = models.EmailField(_('email'))
    user = models.ForeignKey(
        'auth.User', verbose_name=_('user'), blank=True, null=True)

    class Meta:
        verbose_name = _('rival')
        verbose_name_plural = _('rivals')

    def __unicode__(self):
        return self.email
