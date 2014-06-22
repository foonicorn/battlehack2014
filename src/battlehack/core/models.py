import uuid

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
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), max_length=127)
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
    def owner(self):
        return self.attendee_set.get(type=Attendee.TYPE_OWNER)

    @property
    def rival(self):
        return self.attendee_set.get(type=Attendee.TYPE_RIVAL)

    @property
    def pending(self):
        return (
            self.owner.status == Attendee.STATUS_PENDING or
            self.rival.status == Attendee.STATUS_PENDING)


class Attendee(models.Model):
    TYPE_OWNER = 'owner'
    TYPE_RIVAL = 'rival'
    TYPE_CHOICES = (
        (TYPE_OWNER, _('owner')),
        (TYPE_RIVAL, _('rival')),
    )

    STATUS_PENDING = 'pending'
    STATUS_WIN = 'win'
    STATUS_LOOSE = 'loose'
    STATUS_CHOICES = (
        (STATUS_PENDING, _('pending')),
        (STATUS_WIN, _('win')),
        (STATUS_LOOSE, _('loose')),
    )

    challenge = models.ForeignKey(Challenge, verbose_name=_('challenge'))
    uuid = models.CharField(_('uuid'), max_length=255)
    email = models.EmailField(_('email'), blank=True)
    user = models.ForeignKey(
        'auth.User', verbose_name=_('user'), blank=True, null=True)
    type = models.CharField(_('type'), max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(
        _('status'), max_length=20,
        choices=STATUS_CHOICES, default=STATUS_PENDING)

    class Meta:
        verbose_name = _('attendee')
        verbose_name_plural = _('attendee')
        unique_together = ('challenge', 'type')

    def __unicode__(self):
        return self.user and self.user.username or self.email

    @property
    def opponent(self):
        if self.type == self.TYPE_OWNER:
            return self.challenge.rival
        else:
            return self.challenge.owner

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4()
        super(Attendee, self).save(*args, **kwargs)
