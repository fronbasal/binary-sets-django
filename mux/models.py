from django.db import models


class Artist(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True)
    image = models.URLField(blank=True)


class MixTag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    label = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Mix(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    recorded_at = models.DateTimeField(null=True)
    description = models.TextField(blank=True)
    mux_asset_id = models.CharField(max_length=255)
    cover = models.URLField(blank=True)
    tags = models.ManyToManyField(MixTag, blank=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.artist.name, self.title)
