from django.db import models

from languages.models import Language


class Card(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    thumbnail = models.ImageField()
    icon = models.ImageField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)


class WorkArea(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True)
