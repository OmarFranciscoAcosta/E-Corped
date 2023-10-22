from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class CustomUserCreationForm (UserCreationForm):
    pass
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = fields = ['username','first_name', 'last_name', 'email']

class CustomPasswordChangeForm(PasswordChangeForm):
    success_url = '/cambio-contrasena-exitoso/'