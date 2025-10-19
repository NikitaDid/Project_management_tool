from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, profile, users_list

app_name = 'users'
urlpatterns = [
    path('',users_list, name='users_list'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'), name='logout'),
    path('profile/', profile, name='profile'),
]