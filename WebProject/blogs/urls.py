from django.urls import path
from . import views
app_name = "blogs"

urlpatterns = [
    path("", views.blogs_home_view, name="blogs_home_view"),
    path("add/", views.add_blog_view, name="add_blog_view"),
    path("detail/<blog_id>/", views.blogs_details_view, name="blogs_details_view"),
    path("not", views.not_exist, name="not_exist" ),
]


