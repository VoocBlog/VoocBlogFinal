from django.urls import path
from . import views

urlpatterns = [
    path('', views.Error),
    #path('<int:id>/', views.PostDetail),
    path('<int:pk>/', views.Comment, name='comment'),
]