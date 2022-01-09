from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

# forms
from snapserver.forms import PostForm, CustomUserCreationForm, PostCommentForm  # , PostCommentForm

# models
from api.models import Post

from django.contrib.auth import authenticate, login

# services
from . import slicer


def home(request):
    return render(request, 'post/home.html', slicer.slicer())


@login_required
def post_create(request):
    if request.method == 'POST':
        formset = PostForm(request.POST, request.FILES)
        if formset.is_valid():
            post = formset.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.upload)
            post.save()
            messages.success(request, "Post saved. Check in the homepage")
            return redirect("/")
    else:
        formset = PostForm()
    return render(request, 'post/create_post.html', {'form': formset})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    # List of active comments for this post
    comments = post.comments.all()

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = PostCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.author = request.user
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = PostCommentForm
    return render(request, 'post/post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form})


@login_required
def profile(request):
    user = request.user
    posts = user.posts.all()
    name = None
    if not user.first_name or user.first_name == "":
        name = user.email.split("@")[0]
    else:
        name = user.first_name
    return render(request, 'account/profile.html', {'user': user, 'posts': posts, 'name': name})


# signup COMPLETE
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully')
            # user = authenticate(request, username=form['email'], password=form['password'])
            # if user is not None:
            #     login(request, user)
            #     messages.success(request, f"Authenticated as {user.email}")
            # else:
            #     messages.info(request, "You can now login with your credentials")
            #     return redirect("login")
        return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back {username}')
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, f'User {username} Not found')
            return redirect("login")

    return render(request, 'account/login.html')
