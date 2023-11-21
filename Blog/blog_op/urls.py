from django.urls import path
from .import views

app_name = 'blog_op'

urlpatterns =[
    path('add/',views.add_blog,name='add_blog'),
    path('publications/',views.publications,name='publications')
]