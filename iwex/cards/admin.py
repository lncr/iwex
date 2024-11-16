from django.contrib import admin
from cards.models import Card, WorkArea


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', )
    search_fields = ('title', )


@admin.register(WorkArea)
class WorkAreaAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )
