from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from .forms import MusicianForm
from .models import Musician

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'edit_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    
@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'delete_musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')