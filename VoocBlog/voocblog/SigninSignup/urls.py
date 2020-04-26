from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='signin'),
    #path('login/username', view.profile, name='username'),
    path('register/', views.signup, name='signup'),
    path('homepage/', views.logout, name='logout'),
    path('login/index', views.profile, name='profile'),
    path('login/profile', views.loginprofile, name='loginprofile'),
    path('register/error/', views.error, name='error')
    #path('login/', auth_views.LoginView.as_view(template_name = "LoginRegister/sign-in.html"), name='signup'),
]

