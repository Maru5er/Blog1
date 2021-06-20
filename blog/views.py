from django.shortcuts import render
from django.http import HttpResponse
from.models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_time__lte=timezone.now()).order_by('published_time')
    return render(request, 'blog/post_list.html', {'posts':posts})

def homepage(request):
    return render(request,'blog/Index.html',{})
