from django.urls import path
from contacts.views import ContactCreateView

urlpatterns = [
    path('contacts/', ContactCreateView.as_view(), name='create-contact'),
]
