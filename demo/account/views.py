from django.shortcuts import render, redirect
from .form import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def userLogin(request):
    if request.user.is_authenticated: # Checking User is Login in or not
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.error(request, 'Invalid username or password')

    context = {}
    return render(request, 'login.html', context)


def userLogout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'User created successfully for {username}!')
                return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)
