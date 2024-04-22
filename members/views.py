from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in. Try again..."))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})


def customLogout(request):
    logout(request)
    return render(request, 'authenticate/logout.html')  # Render the logout template