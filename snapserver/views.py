from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.text import slugify

# models
from api.models import Post, Following, User
from snapserver.forms import PostForm, CustomUserCreationForm, PostCommentForm  # , PostCommentForm
# services
from . import slicer


# forms


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
            messages.success(request, "Post saved. Check in the homepage", extra_tags='alert')
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


# def post_delete(request, post_slug):
#     # post = get_object_or_404(Post, slug=post_slug)
#     post = Post.objects.get(slug=post_slug)
#     print(post)
#
#     if request.method == 'DELETE':
#         if request.user == post.author:
#             post.delete()
#             messages.success(request, "post deleted")
#     return reverse(home)


@login_required
def profile(request, pk):
    # user = request.user
    # posts = user.posts.all()
    user, _ = User.objects.get_or_create(id=pk)
    print(user)
    posts = user.posts.all()
    count = posts.count()

    following = Following.objects.filter(user=user).count()
    followers = Following.objects.filter(follow=user).count()

    # followers = user.follower.all().count()
    # following = user.followed.all().count()

    name = None
    if not user.first_name or user.first_name == "":
        name = user.email.split("@")[0]
    else:
        name = user.first_name

    return render(request, 'account/profile.html',
                  {'user': user, 'posts': posts, 'name': name, "count": count, "followers": followers,
                   "following": following})


@login_required
def user_following(request):
    if request.method == "POST":
        user = request.user
        to_follow = request.follow
        following = Following.objects.filter(user=user, follow=to_follow)
        is_following = True if following else False

        if is_following:
            Following.delete(following)
            is_following = False
            messages.success(request, f"You unfollowed {request.follow.id}")

        else:
            Following.objects.create(user=user, follow=to_follow)
            is_following = True
            messages.success(request, f"You now follow {request.follow.id}")

        resp = {
            'following': is_following,
        }

        return render(request, "_partials/follow.html", resp)


# signup COMPLETE
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account successfully created for {user.email}', extra_tags='alert')
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
            messages.success(request, f'Welcome back {username}', extra_tags='alert')
            return redirect("/")
        else:
            # Return an 'invalid login' error message.
            messages.warning(request, f'User {username} Not found', extra_tags='alert')
            return redirect("login")

    return render(request, 'account/login.html')
