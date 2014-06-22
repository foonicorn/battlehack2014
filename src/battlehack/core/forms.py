from django import forms

from . import models
from battlehack.paypal.models import Payment


class ChallengeCreateForm(forms.ModelForm):
    rival = forms.EmailField(required=True)

    class Meta:
        model = models.Challenge
        fields = ('title', 'description', 'charity', 'amount')
        widgets = {'charity': forms.RadioSelect}

    def __init__(self, *args, **kwargs):
        super(ChallengeCreateForm, self).__init__(*args, **kwargs)
        self.fields['charity'].empty_label = None

    def save(self, owner, commit=True):
        obj = super(ChallengeCreateForm, self).save(commit=True)
        owner = models.Attendee.objects.create(
            challenge=obj,
            type=models.Attendee.TYPE_OWNER,
            user=owner)
        rival = models.Attendee.objects.create(
            challenge=obj,
            type=models.Attendee.TYPE_RIVAL,
            email=self.cleaned_data['rival'])
        Payment.objects.create(attendee=owner)
        Payment.objects.create(attendee=rival)
        return obj


class AttendeeUpdateForm(forms.ModelForm):

    class Meta:
        model = models.Attendee
        fields = ('status',)
