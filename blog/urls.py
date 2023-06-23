from django.urls import path

from blog.views import PostListView
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('post/', PostListView.as_view(), name='post_list'),
]
