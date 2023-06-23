from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Post


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    extra_context = {
        'object_list': Post.objects.all(),
        'title': 'Все статьи'
    }
