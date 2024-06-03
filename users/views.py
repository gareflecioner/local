from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from users.forms import LoginUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

# Create your views here.
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))