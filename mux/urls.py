from django.urls import path, include
from rest_framework import routers

from mux.views import ArtistViewSet, MixTagViewSet, MixViewSet

router = routers.DefaultRouter()
router.register('artists', ArtistViewSet)
router.register('tags', MixTagViewSet)
router.register('mixes', MixViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
