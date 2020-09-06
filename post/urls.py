from django.urls import path,include
from .views import PostListView,PostCreateView,PostUpdateView,PostDeleteView ,PostDetailView,UserPostListView,SearchResultsView


urlpatterns = [
    path('', PostListView.as_view(), name='post'),
      path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('create/', PostCreateView.as_view(), name='create'),

    # search
    path('search/', SearchResultsView.as_view(), name='search_results'),

    # api
    path('api/', include('post.api.urls'))
]
