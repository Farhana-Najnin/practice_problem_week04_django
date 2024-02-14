from django.shortcuts import render
from album.models import Album


def home(request):
    value = Album.objects.all()
    return render(request,'home.html',{'value': value})