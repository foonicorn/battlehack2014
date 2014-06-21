from rest_framework import generics, permissions

from . import serializers
from .permissions import IsOwner
from battlehack.core.models import Challenge


class ChallengeList(generics.ListAPIView):
    queryset = Challenge.objects.all()
    serializer_class = serializers.ChallengeSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self, *args, **kwargs):
        qs = super(ChallengeList, self).get_queryset(*args, **kwargs)
        return qs.filter(owner=self.request.user)


challenge_list = ChallengeList.as_view()


class ChallengeDetail(generics.RetrieveUpdateAPIView):
    queryset = Challenge.objects.all()
    serializer_class = serializers.ChallengeSerializer
    permission_classes = (IsOwner,)

challenge_detail = ChallengeDetail.as_view()
