from django.urls import path
from . import views



app_name = "blogApp"

urlpatterns = [

    path("read/blog/" , views.read_blog_view , name="read_blog_view"),
    path("add/post" , views.add_post_view , name="add_post_view"),

]