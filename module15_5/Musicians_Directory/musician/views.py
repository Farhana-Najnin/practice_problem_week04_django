from django.shortcuts import render, redirect
from . import forms
# from musician.forms import MusicianForm
# Create your views here.
def addmusician(request):
    if request.method == 'POST':
        musicianform = forms.MusicianForm(request.POST)
        if musicianform.is_valid():
            musicianform.save()
            return redirect('addmusician')
    else:
        musicianform = forms.MusicianForm()
    return render(request,'add_musician.html', {'form' : musicianform})