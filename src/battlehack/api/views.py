from rest_framework import generics

from . import serializers
from battlehack.core.models import Challenge


class ChallengeDetail(generics.RetrieveUpdateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = serializers.ChallengeSerializer

challenge_detail = ChallengeDetail.as_view()
