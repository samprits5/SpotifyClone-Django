from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SongSerializer
from admin.song.models import Song


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
