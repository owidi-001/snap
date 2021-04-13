from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm,ProfileUpdateForm, CreatePostForm

from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


# accounts
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}!. You can now log in with your new account')
        return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})



# def login(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         # Redirect to a success page.
#         messages.success(f'Welcome @{username}')
#         return redirect('home')
#     else:
#         # Return an 'invalid login' error message.
#         messages.warning(f'@{username} not found !!! \n Please register to log in...')
#         return render(request,'registration/register.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    messages.success(f'Successfully logged out. \n Log in to view the site.')
    return redirect('login')

# profile view and update
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account successfully updated ')
            return redirect('post')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'registration/profile.html', context)


# posts
@login_required
def post(request):
    context = Post.objects.all().order_by('-date_posted')[:10]
    return render(request, 'post/index.html',{context:context})


@login_required
def post_create(request):
    if request.method == 'Post':
        form = CreatePostForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Post successfully uploaded. Let\'s view in the blogs')
            return redirect('home')
    else:
        form = CreatePostForm()
    return render(request, 'post/create_post.html', {'form': form})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'upload', 'caption']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.author == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        if self.request.author == post.author:
            return True
        return False
