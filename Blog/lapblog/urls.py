from django.urls import path
from . import views

app_name = "lapblog"

urlpatterns = [ 
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.blog_home_view, name="blog_home_view")

]