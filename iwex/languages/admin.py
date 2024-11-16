from django.contrib import admin
from languages.models import Language


@admin.register(Language)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
