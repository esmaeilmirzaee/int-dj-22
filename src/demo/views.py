from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserRegisterForm, UserLoginForm


def register_user_view(request):
    form = UserRegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            print(user)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            auth_user = authenticate(username=user.username, password=password)
            login(request, auth_user)
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_user_view(request):
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        print('login')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return redirect('/')

    context = {
        'form': form,
    }

    return render(request, 'login.html', context=context)
