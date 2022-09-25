from unicodedata import name
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

from django.contrib.auth.forms import *

from .decorators import *
from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@unauthenticated_user
def signup(request):
    userregisterform = CreateUserForm()
    extraform = UserAddForm()
    if request.method == 'POST':
        userregisterform = CreateUserForm(request.POST)
        extraform = UserAddForm(request.POST)
        if userregisterform.is_valid() & extraform.is_valid():
            user = userregisterform.save()
            extraform = extraform.save(False)
            extraform.user = user
            extraform.save()
            group = Group.objects.get(name='user')
            user.groups.add(group)


            messages.success(request, 'Account was created for' + " " + user.username)
            return redirect('signin')
    context = {'userregisterform':userregisterform, 'extraform': extraform}
    return render(request, 'register.html', context)

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('signin')



@login_required(login_url='signin')
def profile(request):
    user = request.user.userprofile
    form = UserAddForm(instance=user)
    
    # if request.method == 'POST':
    #     form = UserAddForm(request.POST, request.FILES, instance=user)
    #     fm = UserChangeForm(request.POST, instance=request.user)
    #     if form.is_valid():
    #         form.save()

    fm = UserChangeForm(instance=request.user)
    context = {'form':form, 'fm':fm}
    return render(request, 'profile.html', context)

@login_required(login_url='signin')
def update_information(request):
    return render(request, 'updateinformation.html')


@login_required(login_url='signin')
def basic_information(request):
    return render(request, 'basic_info.html')


@login_required(login_url='signin')
def contact_information(request):
    user = request.user.userprofile
    form = UserAddForm(instance=user)
    if request.method == 'POST':
        form = UserAddForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'contact_info.html', context)


def dorp_you(request):
    form = DropYouForm()
    if request.method == 'POST':
        form = DropYouForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'dropyou.html', context)    


@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

