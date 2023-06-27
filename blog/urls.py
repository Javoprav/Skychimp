from django.urls import path
from django.views.decorators.cache import never_cache

from blog.views import *
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path('post/', never_cache(PostListView.as_view()), name='post_list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
