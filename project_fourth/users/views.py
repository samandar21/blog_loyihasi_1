from django.shortcuts import render
from django.views.generic import CreateView,View
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class SignUpView(CreateView):
    form_class=CustomUserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
    

    

    
    