from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
    path("add/", views.addBlog, name="addBlog"),
    path("all/", views.displayBlog, name="displayBlog"),

    
]