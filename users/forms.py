from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        #  model which is affected by this form.
        model = User
        #  fields which are displayed in form.
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        #  model which is affected by this form.
        model = User
        #  fields which are displayed in form.
        fields = ['username','email']
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        #  model which is affected by this form.
        model = Profile
        #  fields which are displayed in form.
        fields = ['image']