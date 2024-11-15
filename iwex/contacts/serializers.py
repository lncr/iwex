import re
from rest_framework import serializers

from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = Contact
        fields = ['id', 'full_name', 'email', 'phone_number', 'subject', 'message']

    def validate_phone_number(self, value):
        """
        Custom validation for phone numbers.
        - Supports international format (e.g., +123456789).
        - Ensures only digits and optional '+' are included.
        """
        if not re.match(r'^\+?\d{7,15}$', value):
            raise serializers.ValidationError(
                "Phone number must be in international format with 7 to 15 digits (e.g., +123456789)."
            )
        return value

    def validate_email(self, value):
        """
        Custom validation for email to ensure domain is valid.
        """
        if not value.endswith(('.com', '.org', '.net')):
            raise serializers.ValidationError(
                "Email must have a valid domain ending in .com, .org, or .net."
            )
        return value
