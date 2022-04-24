from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserLoginForm


def register_user_view(request):
    next_url = request.GET.get('next')
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
            if next_url:
                return redirect(next_url)
            return redirect('/')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login_user_view(request):
    next_url = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if request.method == "POST":
        print('login')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            if next_url:
                return redirect(next_url)
            return redirect('/')

    context = {
        'form': form,
    }

    return render(request, 'login.html', context=context)


def logout_user_view(request):
    logout(request)
    return redirect('/')


def home_view(request):
    return render(request, 'home.html', {})


@login_required
def premium_view(request):
    # if not request.user.is_authenticated:
    #     return redirect('demo:login')
    return render(request, 'premium.html')
