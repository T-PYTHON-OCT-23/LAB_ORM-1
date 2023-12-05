from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Profile
from django.contrib.auth.models import User
# Create your views here.

def edit_profile_view(request:HttpRequest,profile_id):

    if not request.user.has_perm('account.change_profile'):
        return render(request,'account/unauth.html')
    
    if request.method == 'POST':
        user:User = request.user
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        try:
            profile:Profile = request.user.profile
        except:
            profile = Profile(user=user ,image=request.FILES['avatar'],bio=request.POST['bio'])
            profile.save()
        
        profile.bio = request.POST['bio']
        profile.image = request.FILES['avatar']
        profile.save()

        return redirect('account:profile_view',profile_id=request.user.id)

    new_profile = User.objects.get(id=profile_id)

    return render(request, 'account/profile.html',{'user_profile':new_profile})


def profile_view(request:HttpRequest,profile_id):

    profile = User.objects.get(id=profile_id)

    return render(request,'account/profile.html',{'user_profile':profile})