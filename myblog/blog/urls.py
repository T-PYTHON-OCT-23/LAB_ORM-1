# blog/urls.py
from django.urls import path
from .views import post_list, add_post , view_post

app_name = 'blog'

urlpatterns = [
    path('', post_list, name='post_list'),
    path('add', add_post, name='add_post'),
    path('view/<int:post_id>', view_post, name='view_post')
]
