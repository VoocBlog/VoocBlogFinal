from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PostForm
from django import forms

from .models import Post

from django.http import HttpResponse
# Create your views here.

#def post_create_view(request):
#    form = PostForm(request.POST or None, request.FILES)
 #   if form.is_valid():
 #       form.save()
  #  
  #  context = {
  #      'form' : form
    #}
    #return render( request, "blog/blog_create.html", context)
    #
    # form = abc()
    # #raise forms.ValiddationError('asjhd')
    # if request.method=='POST':
    #     form = abc(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/')
    # return render( request, "blog/blog_create.html", {'form' : form} )

# def IsInSession(request):
#     if request.session.has_key('username'):
#         return HttpResponseRedirect('posting-post')
#     else:
#         return HttpResponse('Must login')
        
def post_create_view(request):
    context = {
        "form":PostForm
    }
    return render(request,"blog/blog_create.html", context )
def AddBlog(request):
    form = PostForm(request.POST or None, request.FILES)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return redirect('/')