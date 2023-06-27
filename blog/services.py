from django.conf import settings
from django.core.cache import cache

from blog.models import Post


def blog_cache(obj):
    if settings.CACHE_ENABLED:
        key = 'post'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Post.objects.all()
            cache.set(key, subject_list)
    else:
        subject_list = Post.objects.all()
    return subject_list
