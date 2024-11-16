from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from cards.models import Card, WorkArea
from cards.serializers import CardSerializer, WorkAreaSerializer



class CardReadViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class WorkAreaViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = WorkArea.objects.all()
    serializer_class = WorkAreaSerializer
