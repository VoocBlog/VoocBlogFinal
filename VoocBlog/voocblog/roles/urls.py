from django.urls import path
from . import views


urlpatterns = [
    #path('AddBlog/', views.AddBlog, name='AddBlog'),
    path('blog/', views.post_create_view, name='blog')
    
]