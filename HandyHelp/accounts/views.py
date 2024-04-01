from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ProfileForm, UserForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/signin.html', {'form': form})


@login_required
def profile(request):
    # Отримання поточного користувача
    user = request.user
    # Отримання профілю користувача
    profile = user.profile  # Припустимо, що профіль зв'язаний з користувачем через модель OneToOneField
    return render(request, 'accounts/profile.html', {'user': user, 'profile': profile})


@login_required
def edit_profile(request):
    # Отримання поточного користувача
    user = request.user
    # Отримання профілю користувача
    profile = user.profile  # Припустимо, що профіль зв'язаний з користувачем через модель OneToOneField

    if request.method == 'POST':
        # Якщо користувач відправив форму, оновіть дані профілю
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        # Якщо це GET-запит, створіть форми для редагування профілю
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def home(request):
    # Ваш код для обробки домашньої сторінки
    return render(request, 'accounts/home.html')