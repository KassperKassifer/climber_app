from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect the user back to the stored URL or a default URL
            if 'next' in request.session:
                next_url = request.session.get('next', '/')
                del request.session['next']
            else:
                next_url = reverse('index')
            return redirect(next_url)
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in. Try again..."))
            return redirect('login')

    else:
        return render(request, 'authenticate/login.html', {})


def customLogout(request):
    logout(request)
    return render(request, 'authenticate/logout.html')  # Render the logout template