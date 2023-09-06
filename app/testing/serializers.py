from rest_framework import serializers
from .models import *
from datetime import datetime, date
from django_celery_results.models import TaskResult


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source

class MangaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        exclude = ['active']

class MangaQuerySerializer(serializers.Serializer):
    name = serializers.CharField(required=False,help_text="имя записи")
    status = serializers.CharField(required=False,help_text="статус")
    description = serializers.CharField(required=False,help_text="описание")
    start_date = serializers.CharField(required=False,help_text="Дата начало периодa (10.10.2023)")
    end_date = serializers.CharField(required=False,help_text="Дата начало периодa (10.10.2023)")


class PutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['id','name',]

class MangaListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manga
        fields = ['name', 'id','description','time']





