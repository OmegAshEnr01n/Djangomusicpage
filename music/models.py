# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 100)
    album_title = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 1000)
    def __str__(self):
        return "%s by %s"%(self.album_title,self.artist)
class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title = models.CharField(max_length = 100)
    file_type = models.CharField(max_length = 10)
    isfav = models.BooleanField(default=False)
    def __str__(self):
    	return "%s"%(self.song_title)