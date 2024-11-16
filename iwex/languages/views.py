from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from languages.models import Language
from languages.serializers import LanguageSerializer


class LanguageReadViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
