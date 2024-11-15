from django.db import models


class Contact(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=400, verbose_name='Full name')
    email = models.CharField(max_length=255, verbose_name='Email')
    phone_number = models.CharField(max_length=50, verbose_name='Phone Number')
    subject = models.CharField(max_length=255, verbose_name='Subject')
    message = models.TextField(blank=True)

    def __str__(self):
        return f"{self.email} ({self.phone_number})"
