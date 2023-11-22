from . import views
from django.urls import path ,include

app_name = 'blogs'

urlpatterns = [
    path('add/',views.add_blogs_views,name='add_blogs_views'),
    path('',views.show_blogs_views,name='show_blogs_views'),
    path('detils/<mo_id>/', views.show_blogs_detils_view,name='show_blogs_detils_view')
]