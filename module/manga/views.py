from rest_framework import generics
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404
# Create your views here.
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

from module.manga.models import Manga, Chapter
from module.manga.serializers import MangaListSerializer, ChapterSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView, exception_handler


class MangaListAPIView(generics.ListCreateAPIView, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MangaListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Manga.objects \
            .prefetch_related('chapter') \
            .prefetch_related('chapter__image').filter()

    def post(self, response):
        data = self.serializer_class.data


class MangaListView(generics.ListCreateAPIView):
    serializer_class = MangaListSerializer
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Manga.objects \
            .prefetch_related('chapter') \
            .prefetch_related('chapter__image').filter()

    def get(self, request):
        queryset = self.get_queryset()
        if request.accepted_renderer.format == 'html':
            context = {'serializer': MangaListSerializer,
                       'sth': queryset}
            return Response(context, template_name='manga/view.html')
        serializer = MangaListSerializer(instance=queryset)
        data = serializer.data
        return Response(data)

