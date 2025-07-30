from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserUpdateForm
from django.conf import settings  
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')

def doctor_profile(request):
    return render(request, 'doctor_profile.html')

def register(request):
    return render(request, 'register.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('profile')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})
