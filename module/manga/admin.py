from django.contrib import admin
from module.manga.models import *


@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated', 'created')
    list_filter = ('name', 'created', 'updated')
    search_fields = ('id', 'name')


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name',  'manga', 'updated','created')
    list_filter = ('name', 'manga', 'created', 'updated')
    search_fields = ('id', 'name')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'chapter', 'created', 'updated')
    list_filter = ('id', 'image', 'created', 'updated')
