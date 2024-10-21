from rest_framework import permissions, viewsets

from mux.models import Artist, MixTag, Mix
from mux.permissions import IsAdminOrReadOnly
from mux.serializers import ArtistSerializer, MixTagSerializer, MixSerializer


class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (IsAdminOrReadOnly,)


class MixTagViewSet(viewsets.ModelViewSet):
    queryset = MixTag.objects.all()
    serializer_class = MixTagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class MixViewSet(viewsets.ModelViewSet):
    queryset = Mix.objects.all()
    serializer_class = MixSerializer
    permission_classes = (IsAdminOrReadOnly,)
