from django.db import models


class Songer(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Album(models.Model):
    songer = models.ForeignKey(
        Songer,
        on_delete=models.CASCADE,
    )
    year = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Songs(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songs',
    )
    name_music = models.CharField(max_length=40)
    number = models.IntegerField()

    def __str__(self):
        return self.name_music

