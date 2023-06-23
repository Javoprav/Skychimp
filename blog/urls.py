from django.urls import path
from django.views.decorators.cache import never_cache

from blog.views import *
from blog.apps import BlogConfig

app_name = BlogConfig.name


urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', never_cache(PostCreateView.as_view()), name='post_create'),
    path('posts/update/<int:pk>/', never_cache(PostUpdateView.as_view()), name='post_update'),
    path('posts/delete/<int:pk>/', never_cache(PostDeleteView.as_view()), name='post_delete'),
]
