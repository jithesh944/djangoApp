from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'jithesh',
#         'title': 'Blog Post 1',
#         'content': 'Django started.. good concepts',
#         'date_posted': 'Februry 20, 2021'
#     },
#     {
#         'author': 'Jithesh',
#         'title': 'Blog Post 2',
#         'content': 'Django continuing.. easily understandable',
#         'date_posted': 'Feb 23, 2021'
#     }
# ]
# Create your views here.
def home(request):
    """
    simple func to route from home
    """
    content_post = {
        'user_post': Post.objects.all()
    }
    return render(request,'blog/home.html',content_post)


def blog_about(request):
    """
    simple page to describe
    """

    return render(request,'blog/about.html',{'title' :'About webpage'})