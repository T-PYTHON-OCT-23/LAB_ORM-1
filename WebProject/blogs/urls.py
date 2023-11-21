from django.urls import path
from . import views
app_name = "blogs"


urlpatterns = [
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("", views.blogs_home_view, name="blogs_home_view")
]


