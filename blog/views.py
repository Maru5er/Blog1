from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from.models import Post, Comment
from django.utils import timezone
from .forms import PostForm, Registration, PostComment
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_time__lte=timezone.now()).order_by('published_time')
    return render(request, 'blog/post_list.html', {'posts':posts})


def homepage(request):
    return render(request,'blog/Index.html',{})


def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    new_comment = None
    comments = post.comments.filter(active = True)
    if request.method == "POST":
        form = PostComment(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostComment()
    return render(request, 'blog/post_detail.html', {'form': form,
                                                     'post':post,
                                                     'new_comment': new_comment,
                                                     'comments': comments})


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
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successfull!')
            return redirect('post_list')
        messages.error(request, 'Failed registration. Invalid info.')
        return render(request, 'blog/registration.html', {'form': form})

    else:
        form = Registration()
    return render(request, 'blog/registration.html', context={'form': form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.info(request, 'welcome, you are now logged in as {}'.format(username))
                return redirect('post_list')
            else:
                messages.error(request, 'Invalid Username or Password')
        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_request(request):
    logout(request)
    return redirect('post_list')











