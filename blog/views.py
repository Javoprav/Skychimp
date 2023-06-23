from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from blog.models import Post
from django.http import Http404


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    extra_context = {
        'object_list': Post.objects.all(),
        'title': 'Все статьи'
    }

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = self.get_object()
        obj = self.get_object()
        increase = get_object_or_404(Post, pk=obj.pk)
        increase.increase_views()
        return context_data


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'slug', 'content', 'preview', 'created_by')
    success_url = reverse_lazy('blog:post_list')


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'slug', 'content', 'preview',)

    def get_success_url(self):
        return reverse('blog:post_detail', args=[str(self.object.slug)])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
