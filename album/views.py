from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .forms import AlbumForm
from .models import Album

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    
@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')