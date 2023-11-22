from django.urls import path
from . import views
app_name = "Blogs"
urlpatterns = [
    path('read/',views.read,name='read_blog'),
    path('add/',views.add,name='add_blog')
]