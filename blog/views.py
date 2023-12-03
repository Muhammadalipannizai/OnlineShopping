from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost

def index(request):
    mypost=Blogpost.objects.all()
    # print(mypost)
    return render(request,'blog/index.html',{'mypost':mypost})


def blogPost(request , id):
    post=Blogpost.objects.filter(post_id=id)
    # print(post)
    return render(request, 'blog/blogpost.html',{'post':post[0]}) 
