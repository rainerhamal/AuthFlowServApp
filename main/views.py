from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
# request handler

@login_required(login_url='/login')
def home(request):
    return render(request, 'main/home.html')

def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = UserForm()

    return render(request, 'registration/sign_up.html', {"form": form})