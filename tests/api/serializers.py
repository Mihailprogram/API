from rest_framework import serializers

from .models import Album, Songer, Songs


class SongerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songer
        fields = ('id', 'name')


class SongsSerializer(serializers.ModelSerializer):
    album = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Album.objects.all(),
    )

    class Meta:
        model = Songs
        fields = ('id', 'name_music', 'number', 'album')


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = ('name_music',)


class AlbumSerializer(serializers.ModelSerializer):
    songer = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Songer.objects.all(),
    )

    songs = MusicSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'name', 'year', 'songer', 'songs')
