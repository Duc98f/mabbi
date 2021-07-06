from django.urls import path

from .views import *

urlpatterns = [
    # url(r'', UsersView.as_view(), name='list-user'),
    path('api/v1/manga/', MangaListAPIView.as_view(), name='manga'),
    path('', MangaListView.as_view(), name='home'),
]
