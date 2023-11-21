from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [ 
    path("add/",views.add_blog_views, name="add_blog_views"),
    path("", views.home_blog_views, name="home_blog_views"),


]