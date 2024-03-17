from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django import forms
import os
from django.core.files.storage import default_storage
def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account is successfully created for {username}.Now you can login')
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    if request.POST:
         old_image_path = request.user.profile.image.url
         if os.path.isfile(old_image_path):
                os.remove(old_image_path)
         u_form=UserUpdateForm(request.POST,instance=request.user)
         p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
         if u_form.is_valid() and p_form.is_valid():
             
            #  post.author.profile.image.url=request.user.profile.image.url
             u_form.save()
             p_form.save()
             messages.success(request,f'Your account has been updated!')
             return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)



   
    context={  'u_form':u_form, 'p_form':p_form,'filter1':default_storage.exists(request.user.profile.image.name)}
    return render(request,'users/profile.html',context)