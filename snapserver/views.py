from api.models import Post
from django.shortcuts import render
from django.http import Http404

# forms
from api.forms import PostUpdateForm, PostCommentForm

# services
from . import slicer


def home(request):
    return render(request, 'post/home.html', slicer.slicer())


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


def post_comment(request, pk):
    try:
        obj = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        raise Http404("No Post matches the given query.")

    if request.method == 'POST':
        form = PostCommentForm(request.POST, instance=request.user)
        if form.is_valid():
            form.comment_by = request.user
            form.post = obj
            form.save()
            return HttpResponseRedirect(reverse(pk))
    return HttpResponse('post-detail')


def profile(request):
    return render(request, 'account/profile.html')
