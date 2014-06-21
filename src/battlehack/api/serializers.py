from rest_framework import serializers

from battlehack.core import models


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Challenge
        fields = ('id', 'title', 'description', 'charity', 'amount')
