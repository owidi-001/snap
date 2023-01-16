from django.urls import path

from .views import PortView

urlpatterns=[
    path('post', PortView.as_view(),name="posts"),
]