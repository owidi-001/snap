from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)


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


# profile view and update
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Account successfully updated ')
            return redirect('post')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }
    return render(request, 'registration/profile.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'snapserver/index.html'
    fields = ['title', 'upload', 'caption']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.author
        return super().form_valid(form)


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
