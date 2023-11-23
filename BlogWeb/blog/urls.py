from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [ 
    path("add/",views.add_blog_views, name="add_blog_views"),
    path("", views.home_blog_views, name="home_blog_views"),
    path("details/<blog_id>/", views.details_blog_views, name="details_blog_views"),
    path("updated/<blog_id>/", views.updated_blog, name="updated_blog"),
    path("delete/<blog_id>/", views.delete_blog_views ,name="delete_blog_views")
]