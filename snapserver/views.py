from api.models import Post
from django.shortcuts import render
from django.http import Http404

# forms
from api.forms import PostUpdateForm


def home(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'post/home.html', {'posts': posts})


def post_create(request):
    return render(request, 'post/create_post.html')


def post_detail(request, pk):
    try:
        obj = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("No Post matches the given query.")

    # update and delete
    if request.user == obj.author:
        u_form = PostUpdateForm()
        if u_form.is_valid():
            post = u_form.cleaned_data.save()
        else:
            U_form = PostUpdateForm()

    return render(request, 'post/post_detail.html', {'post': obj})


def profile(request):
    return render(request, 'account/profile.html')
