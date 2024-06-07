from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from album.models import Album
from .forms import SignUpForm

# Create your views here.
def home(request):
    data = Album.objects.all() 
    return render(request, 'home.html', {'data': data})

def signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect ('home')
    else:
        signup_form = SignUpForm(request.POST)
        
    return render(request, 'authentication.html', {'form': signup_form, 'heading': 'Create New Account', 'btn_text': 'Create'})

class UserLoginView(LoginView):
    template_name = 'authentication.html'
    
    def get_success_url(self): 
        return reverse_lazy('home')    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successfully!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Login information is incorrect!')
        return super().form_invalid(form)    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Login to Your Account'
        context['btn_text'] = 'Login'
        return context  
    
@login_required 
def user_logout(request):
    logout(request)
    return redirect('home')