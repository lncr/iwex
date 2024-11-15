from rest_framework.generics import CreateAPIView
from contacts.models import Contact
from contacts.serializers import ContactSerializer


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
