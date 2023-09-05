from rest_framework import routers

from api.views import SongerViewSet, SongsViewSet, AlbumViewSet

from django.urls import include, path

router = routers.DefaultRouter()

router.register('songer', SongerViewSet, basename='songer')
router.register('songs', SongsViewSet, basename='songs')
router.register('album', AlbumViewSet, basename='album')

urlpatterns = [
    path('v1/', include(router.urls)),
]
