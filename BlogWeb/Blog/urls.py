from django.urls import path
from . import views
app_name = "Blog"
urlpatterns = [
    path('read/',views.read_blog,name='read_blog'),
    path('add/',views.add_blog,name='add_blog')
]
