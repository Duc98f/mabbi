from rest_framework import serializers
import os, uuid, requests
from django.conf import settings
from module.manga.models import *


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ChapterSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class MangaListSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(many=True)

    class Meta:
        model = Manga
        fields = '__all__'
