'''
TO DO:
RELATE CREATE VIEWS WITH THE FORMS
CREATE LIKE VIEW AND ADD LOGIC FOR THE COUNTS
'''

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post, Comment, Likes
from django.contrib.auth.models import User
# from accounts.models import profile
from django.urls import reverse_lazy
# search bar
from django.db.models import Q


# post views
class PostListView(ListView, LoginRequiredMixin):
    model = Post
    template_name = 'snapserver/index.html'
    context_object_name = 'posts'
    success_url = reverse_lazy('post')
    ordering = ['-date_posted']
    paginate_by = 10


class UserPostListView(ListView):
    model = Post
    template_name = 'post/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date_posted')


class UserProfilePostListView(ListView):
    model = Post
    template_name = 'registration/profile.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(user=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/Post_detail.html'
    # success_url = reverse_lazy('post')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post/Post_form.html'
    fields = ['upload', 'caption']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['upload', 'caption']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post')

    # success_url='post'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


# comments views
class CommentListView(ListView, LoginRequiredMixin):
    model = Comment
    template_name = 'post/post.html'
    context_object_name = 'comments'
    success_url = reverse_lazy('post')
    ordering = ['-date_added']
    paginate_by = 3


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'post/post.html'
    fields = ['body']
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('post')

    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.user:
            return True
        return False


# search filters

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
