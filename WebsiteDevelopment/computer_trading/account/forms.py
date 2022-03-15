from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth.models import User



class CustomUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'username', 'email']