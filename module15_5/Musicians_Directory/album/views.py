from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def addalbum(request):
    if request.method == 'POST':
        albumform = forms.AlbumForm(request.POST)
        if albumform.is_valid():
            albumform.save()
            return redirect('addalbum')
    else:
        albumform = forms.AlbumForm()
    return render(request,'add_album.html',{'form' : albumform})


def editalbum(request,id):
    album = models.Album.objects.get(pk=id)
    albumform = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        albumform = forms.AlbumForm(request.POST)
        if albumform.is_valid():
            albumform.save()
            return redirect('homepage')
        
    return render(request,'add_album.html',{'form' : albumform})


def deletealbum(request,id):
    album = models.Album.objects.get(pk=id)
    album.delete()
    return redirect('homepage')
   
