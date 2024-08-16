from django.urls import path

from app.views import index, posts, post_info, post_id, delete_posts, add_posts

urlpatterns = [
    path('index', index),
    path('', posts, name='main'),
    path('post/<int:post_id>', post_info, name='post_info'),
    path('post_id', post_id, name='post_id'),
    path('delete_posts', delete_posts, name='delete_posts'),
    path('add_posts', add_posts, name='add_posts')
]
