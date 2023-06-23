from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from .models import User2
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.
# request handler

@login_required(login_url='/login')
def home(request):
    #get the current user
    user = request.user

    users = User.objects.all()
    
    # check if user has admin role
    # is_admin = user.is_staff or user.is_superuser

    # if is_admin:
    #     return render(request, 'home/admin_site.html')

    # else:
    #     return redirect('home')
    #get all permissions available for the user
    permissions = user.user_permissions.all()

    # create list of permission names
    permission_names = [permission.codename for permission in permissions]

    context = {
        'permission_names': permission_names,
        'users': users,
    } 

    return render(request, 'main/home.html', context)


def sign_up(request):   
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user = get_user_model().objects.authenticate(username=user2.username, password=user2.password)
            login(request, user)
            return redirect('/home')

    else:
        form = UserForm()

    return render(request, 'registration/sign_up.html', {"form": form})



def user_update(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = UserForm()
        else:
            user = request.user
            user_info = User.objects.get(pk=id)
            form = UserForm(instance=user_info)
        return render(request, 'registration/user_update.html', {"form": form})

    else:
        user_info = User.objects.get(pk=id)
        form = UserForm(request.POST, instance=user_info)
        if form.is_valid():
            user = form.save()
            user_info.__dict__.update(**user.__dict__)
            user_info.save()
            return HttpResponseRedirect('/home')
        else:
            return render(request, 'registration/user_update.html', {"form": form})

            



    