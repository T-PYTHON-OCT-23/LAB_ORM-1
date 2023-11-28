from django.urls import path
from . import views

app_name = "index"

urlpatterns = [
    path("add/",views.add_view,name="add_view"),
    path("",views.home_view,name="home_view")
]