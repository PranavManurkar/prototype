from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('accounts/home.html')  # Redirect to home page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # 'password1' is the first password field
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('')  # Redirect to home page after successful signup and login
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def home_view(request):
    return render(request, 'accounts/home.html')
