from django.urls import path

from cards.views import CardReadViewSet, WorkAreaViewSet


urlpatterns = [
    path('cards/', CardReadViewSet.as_view(), name='card-list'),
    path('workareas/', WorkAreaViewSet.as_view(), name='workarea-list'),
]
