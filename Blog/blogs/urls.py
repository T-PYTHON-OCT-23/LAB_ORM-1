from django.urls import path
from . import views
app_name = "blogs"
urlpatterns = [
    path('read/',views.read,name='read'),
    path('add/<blog_id>/',views.add,name='add')
]