from django import forms
from django.forms import ModelForm
from .models import User, Role, Permission, UserHasRole, RoleHasPermission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password', 'email' ]