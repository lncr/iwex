from django.urls import path
from languages.views import LanguageReadViewSet


urlpatterns = [
    path('languages/', LanguageReadViewSet.as_view({'get': 'list'}), name='language-list'),
]
