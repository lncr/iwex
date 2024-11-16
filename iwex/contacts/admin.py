from django.contrib import admin
from contacts.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone_number')
    search_fields = ('email', 'phone_number')
