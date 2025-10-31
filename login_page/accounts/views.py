from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

        user_auth = authenticate(username=user.username, password=password)
        if user_auth:
            login(request, user_auth)
            return redirect('success')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})

    return render(request, 'login.html')


def signup_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(email=email).exists():
            return render(request, 'signup.html', {'error': 'Email already exists'})

        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        Token.objects.create(user=user)
        return redirect('login')

    return render(request, 'signup.html')


@login_required
def success_view(request):
    token, _ = Token.objects.get_or_create(user=request.user)
    return render(request, 'success.html', {"message": "You are logged in successfully!", "token": token.key})


def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('login')
