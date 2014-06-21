from django import forms

from . import models


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
        obj = super(ChallengeCreateForm, self).save(commit=False)
        obj.owner = owner
        obj.save()
        models.Rival.objects.create(
            challenge=obj, email=self.cleaned_data['rival'])
        return obj
