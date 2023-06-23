from django import forms
from django.forms import ModelForm
from .models import User2, Role, Permission, UserHasRole, RoleHasPermission
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
        # return user
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'password', 'email' ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# class RoleForm(Role):
    