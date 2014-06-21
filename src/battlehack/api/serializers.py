from rest_framework import serializers

from battlehack.core import models


class ChallengeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Challenge
        fields = (
            'owner', 'id', 'title', 'description', 'charity', 'amount',
            'date_created', 'date_updated')
