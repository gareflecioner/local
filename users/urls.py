from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
app_name = "users"

urlpatterns = [
    path('profile/profile-update/', views.ProfileUser.as_view(template_name="users/profile_update.html"), name='profile_update'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('password-change/', views.UserPasswordChange.as_view(template_name="users/password_change_form.html"), name="password_change"),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"), name="password_change_done"),
]

