from rest_framework import serializers

from cards.models import Card, WorkArea


class CardSerializer(serializers.ModelSerializer):

    language = serializers.CharField(source='language.short_name')

    class Meta:
        model = Card
        fields = ['id', 'title', 'text', 'thumbnail', 'icon', 'language', ]



class WorkAreaSerializer(serializers.ModelSerializer):

    language = serializers.CharField(source='language.short_name')

    class Meta:
        model = WorkArea
        fields = ['id', 'name', 'icon', 'language', ]
