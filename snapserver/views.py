from api.models import Post
from django.shortcuts import render, get_object_or_404,redirect
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages

# forms
from api.forms import PostUpdateForm, PostCommentForm, PostCreateForm, CustomUserCreationForm

# services
from . import slicer


def home(request):
    return render(request, 'post/home.html', slicer.slicer())


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            print(post)
            post.save()
            messages.success('Post created successfully')
        return redirect('home')
    else:
        form = PostCreateForm(request.POST)
        print('Submit failed')
    return render(request, 'post/create_post.html', {'form': form})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render(request, 'post/post_detail.html', {'post': post})


@login_required
def post_comment(request, post_slug):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_by = request.user
            comment.post = post_slug.id
            comment.save()
            return redirect(post_slug)
    else:
        form = PostCommentForm()

    return HttpResponse('post-detail', {'form': form})


@login_required
def profile(request):
    user = request.user
    posts = user.posts.all()
    return render(request, 'account/profile.html', {'user': user, 'posts': posts})


# signup
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            # user = authenticate(request, username=user['email'], password=user['password'])
            # if user is not None:
            #     login(request, user)
        return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})
