from django.urls import path
from . import views

app_name = 'account'


urlpatterns = [
    path('edit/<profile_id>',views.edit_profile_view,name='edit_profile_view'),
    path('profile/<profile_id>',views.profile_view,name='profile_view'),

]