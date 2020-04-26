from django.shortcuts import render
from roles.models import Post

#Create your views here.



def PostDetail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'detail/detailpost.html', {'DetailPost' : post})

def Error(request):
    return render(request, 'page/error.html')