from .forms import RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, 'Başarıyla giriş yaptınız.')
                return redirect('home')
            else:
                pass
                #messages.error(request, 'Geçersiz kullanıcı adı veya şifre.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            #messages.success(request, 'Başarıyla kayıt oldunuz.')
            return redirect('home')
    else:
        form = RegisterForm()
    #messages.error(request, 'Kayıt işlemi sırasında hata! Lütfen tekrar deneyiniz.')
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
