from .serializers import AlbumSerializer, SongerSerializer, SongsSerializer
from .models import Album, Songer, Songs

from rest_framework import viewsets


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongerViewSet(viewsets.ModelViewSet):
    queryset = Songer.objects.all()
    serializer_class = SongerSerializer


class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
