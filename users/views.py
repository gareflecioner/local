from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate,login,logout
from users.forms import ProfileUserForm, RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView,PasswordChangeView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model


# Create your views here.
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}
    login_url = '/users/profile/'

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('users:login')
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}
    success_url = reverse_lazy('profile')
 
    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])
        
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        try:
            self.object.update()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("profile_update", kwargs={"pk": self.object.pk})
            )
    
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    extra_context = {'title': "Изменение пароля"}

    def form_valid(self, form):
        try:
            self.object.update()
            return HttpResponseRedirect(self.success_url)
        except Exception as e:
            return HttpResponseRedirect(
                reverse("profile_update", kwargs={"pk": self.object.pk})
            )