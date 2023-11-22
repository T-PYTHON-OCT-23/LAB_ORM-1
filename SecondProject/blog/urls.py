from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.read_blog_view, name="read_blog_view"),

]
