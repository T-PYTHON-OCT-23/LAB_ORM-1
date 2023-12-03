from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def create_user_view(request:HttpRequest):

    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['user_name'],first_name=request.POST["first_name"], last_name=request.POST["last_name"],email=request.POST['email'],password=request.POST['password'])
        user.save()
    
    return render(request,'users/regiostraction.html')


def login_user_view(r):

    if r.method == 'POST':
        msg = None
        user = authenticate(r,username=r.POST['user_name'],password=r.POST['password'])

        if user is not None:
            login(r,user)
            return redirect('blogs:show_blogs_views')
        else:
            msg = "Please provide correct username and password"
        
    return render(r,'users/login.html')

def logout_view(r:HttpRequest):

    if r.user.is_authenticated:
        logout(r)
    
    return redirect('blogs:show_blogs_views')