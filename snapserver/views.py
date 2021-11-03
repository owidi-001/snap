from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.text import slugify

# forms
from api.forms import PostForm, CustomUserCreationForm  # , PostCommentForm

# models
from api.models import Post
from api.models import User

# services
from . import slicer


def home(request):
    return render(request, 'post/home.html', slicer.slicer())


# @login_required
# def post_create(request):
#     title = None;
#     if request.method == 'POST':
#         form = PostCreateForm(data=request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.slug = slugify(post.title)
#             print(post)
#             post = post.save()
#             print(post)
#             messages.success('Post created successfully')
#             return redirect(post.slug)
#         return render(request, 'post/create_post.html', {'form': form})
#     else:
#         print(title)
#         form = PostCreateForm(request.POST)
#         print('Submit failed')
#     return render(request, 'post/create_post.html', {'form': form})


@login_required
def post_create(request):
    # PostFormSet = modelformset_factory(Post, fields=('upload', 'title', 'caption'))
    if request.method == 'POST':
        formset = PostForm(request.POST)
        if formset.is_valid():
            post = formset.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.save()
            messages.success("Post saved")
            return redirect(post.slug)
    else:
        formset = PostForm()
    return render(request, 'post/create_post.html', {'form': formset})


def post_detail(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    # comments = post.comments.filter(active=True)
    # new_comment = None
    # # Comment posted
    # if request.method == 'POST':
    #     comment_form = PostCommentForm(data=request.POST)
    #     if comment_form.is_valid():
    #         # Create Comment object but don't save to database yet
    #         new_comment = comment_form.save(commit=False)
    #         # Assign the current post to the comment
    #         new_comment.post = post
    #         # Save the comment to the database
    #         new_comment.save()
    # else:
    #     comment_form = PostCommentForm()
    return render(request, 'post/post_detail.html', {'post': post})


# @login_required
# def post_comment(request, post_slug):
#     if request.method == 'POST':
#         form = PostCommentForm(request.POST)
#
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.comment_by = request.user
#             comment.post = post_slug.id
#             comment.save()
#             return redirect(post_slug)
#     else:
#         form = PostCommentForm()
#
#     return HttpResponse('post-detail', {'form': form})
#

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
