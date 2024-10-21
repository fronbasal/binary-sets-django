from rest_framework import serializers

from mux.models import Artist, MixTag, Mix


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = (
            "id",
            "created_at",
            "name",
            "bio",
            "birthdate",
            "image",
        )


class MixTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MixTag
        fields = (
            "id",
            "created_at",
            "label",
            "description",
        )


class MixSerializer(serializers.HyperlinkedModelSerializer):
    artist = ArtistSerializer()
    tags = MixTagSerializer(many=True)

    class Meta:
        model = Mix
        fields = (
            "id",
            "title",
            "artist",
            "created_at",
            "recorded_at",
            "description",
            "mux_asset_id",
            "cover",
            "tags",
            "is_public",
        )
