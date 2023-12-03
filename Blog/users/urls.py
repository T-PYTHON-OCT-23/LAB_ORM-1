from django.urls import path
from . import views


app_name = 'users'


urlpatterns = [
    path('register/',views.create_user_view,name='create_user_view'),
    path('login/',views.login_user_view,name='login_user_view'),
    path('logout/',views.logout_view,name='logout_view')
]