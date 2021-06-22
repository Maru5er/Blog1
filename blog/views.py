from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from.models import Post
from django.utils import timezone
from .forms import PostForm, Registration
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_time__lte=timezone.now()).order_by('published_time')
    return render(request, 'blog/post_list.html', {'posts':posts})

def homepage(request):
    return render(request,'blog/Index.html',{})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_time = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, 'Registration successfull!')
            return redirect('post_list')
        messages.error(request, 'Failed registration. Invalid info.')
        form = Registration
        return render(request, 'blog/registration.html', {'register_form': form})


