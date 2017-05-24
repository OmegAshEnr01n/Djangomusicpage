# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Album,Song
from django.template import loader



# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'All': all_albums,
    }
    return HttpResponse(template.render(context, request))

def information(request,album_id):
    try:
        album = Album.objects.get(pk = album_id)
        context = {
            'album': album,
            'counter': 0,
        }
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request,'music/album_info.html',context)
    '''
    Can be replaced.
    album = get_object_or_404(Album, pk=album_id)
    context = {
        'album': album,
        'counter':0,
    }
    return render(request,'music/album_info.html', context)
    '''

def favorite(request,album_id):
    album = get_object_or_404(Album,pk=album_id)
    # song1 = album.song_set.get(pk=4)
    # x=request.POST['%s'%song1.pk]
    # x=request.POST['song']
    try:
        song1 = album.song_set.get(pk=request.POST['song'])
        
    except (KeyError, Song.DoesNotExist):
        context = {
            'album':album,
            'error_message':'lol some error bro!',
            
        }
        return render(request, 'music/album_info.html',context)
    else:
        song1.isfav = True
        song1.save()
        return render(request, 'music/album_info.html',{
                'album':album,
                'song_pk': request.POST['fav_button']
            })