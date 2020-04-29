from django.shortcuts import render, get_object_or_404
from roles.models import Post, Interaction
from django.contrib.auth.models import User
from .forms import CommentForm
from django.http import HttpResponseRedirect

#Create your views here.

# def PostDetail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'detail/detailpost.html', {'DetailPost' : post})

def Error(request):
    return render(request, 'page/error.html')

    
def Comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    # if request.session.has_key('username'):
    #     loginUser = request.session['username']
    #     query = User.objects.filter(username = loginUser)
    return render(request, "detail/detailpost.html", {"DetailPost": post, "form": form})