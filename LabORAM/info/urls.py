from django.urls import path
from . import views

app_name = "info"

urlpatterns = [ 
    path("add/", views.add_info_view, name="add_info_view"),
    path("", views.info_home_view, name="info_home_view"),
    path("detail/<info_id>/",views.info_details_view,name="info_details_view"),
]