from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index),
    path('login/', views.login, name='signin'),
    path('register/', views.signup, name='signup'),
    path('login/profile/', views.profile, name='profile'),
    path('register/error/', views.error, name='error')
    #path('login/', auth_views.LoginView.as_view(template_name = "LoginRegister/sign-in.html"), name='signup'),
]

