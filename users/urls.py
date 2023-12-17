from . import views
from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views


app_name = "users"

urlpatterns = [
    path('profile/', views.profile, name="users-profile"),
    path('my_posts/', views.my_posts, name='users-my_posts'),
    path('register/', views.register, name='users-register'),
    path('login/', CustomLogin.as_view() , name="users-login"),
    path('update_profile/', views.update_profile, name='users-update_profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html') , name="users-logout"),
] 