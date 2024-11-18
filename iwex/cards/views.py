from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics

from cards.models import Card, WorkArea
from cards.serializers import CardSerializer, WorkAreaSerializer


class LanguageFilterMixin:

    def get_queryset(self):
        short_name = self.request.query_params.get('lng')
        queryset = super().get_queryset()
        if short_name is not None:
            queryset = queryset.filter(language__short_name__iexact=short_name.lower())
        return queryset

    @swagger_auto_schema(
        operation_description="Retrieve a list of objects",
        manual_parameters=[
            openapi.Parameter(
                'lng',
                openapi.IN_QUERY,
                description="Query param to short name of language for data",
                type=openapi.TYPE_STRING,
                required=False,
            )
        ]
    )
    def get(self, request):
        return super().get(request)

class CardReadViewSet(LanguageFilterMixin, generics.ListAPIView):
    queryset = Card.objects.all().select_related('language')
    serializer_class = CardSerializer


class WorkAreaViewSet(LanguageFilterMixin, generics.ListAPIView):
    queryset = WorkArea.objects.all().select_related('language')
    serializer_class = WorkAreaSerializer
