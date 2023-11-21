from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [ 
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.post_home_view, name="post_home_view")

]