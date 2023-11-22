from django.urls import path
from . import views

app_name="blogs"

urlpatterns = [

    path("add/" , views.add_blogs_view, name="add_blogs_view"),
    path("", views.show_blogs_view, name="show_blogs_view")
    
]