from django.urls import path
from . import views, blog

app_name = "blog"

urlpatterns = [
    path("add/", views.add_blog, name="add_blog"),
    path("read/", views.read_blog, name="read_blog")

]
