from django.urls import path,include
from .views import (
    # posts
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    UserPostListView,
    UserProfilePostListView,
    # comments
    CommentListView,
    CommentCreateView,
    CommentDeleteView,
    SearchResultsView,
)

urlpatterns = [
    # post routes
    path('', PostListView.as_view(), name='post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('user/<str:username>', UserProfilePostListView.as_view(), name='user-profile-posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('create/', PostCreateView.as_view(), name='create'),

    # comments routes
    path('', CommentListView.as_view(), name='comment'),
    path('comment/', CommentCreateView.as_view(), name='add_comment'),
    path('<int:pk>/delete/', CommentDeleteView.as_view(), name='delete_comment'),

    # search
    path('search/', SearchResultsView.as_view(), name='search_results'),

    # api
    path('api/', include('post.api.urls'))
]
