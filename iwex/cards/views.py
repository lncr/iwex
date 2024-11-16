from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from cards.models import Card, WorkArea
from cards.serializers import CardSerializer, WorkAreaSerializer


class LanguageFilterMixin:

    def get_queryset(self):
        short_name = self.query_params.get('lng')
        queryset = super().get_queryset()
        if short_name is not None:
            queryset = queryset.filter(language__short_name=short_name)
        return queryset

class CardReadViewSet(LanguageFilterMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = Card.objects.all().select_related('language')
    serializer_class = CardSerializer


class WorkAreaViewSet(LanguageFilterMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = WorkArea.objects.all().select_related('language')
    serializer_class = WorkAreaSerializer
