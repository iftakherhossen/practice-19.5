from django.shortcuts import render, redirect
from . import forms
from .models import Album

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect ('add_album')
    else:
        album_form = forms.AlbumForm(request.POST)
        
    return render(request, 'add_album.html', {'form': album_form})

def edit_album(request, id):
    album = Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=album)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=album)
        if album_form.is_valid():
            album_form.save()
            return redirect ('home')
        
    return render(request, 'edit_album.html', {'form': album_form})

def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect('home')