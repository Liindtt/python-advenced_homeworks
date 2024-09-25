from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Реєстрація пройшла успішно!')
            return redirect('login')  # Перенаправлення на головну сторінку
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# Вигляд для профілю користувача
@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def user_logout(request):
    logout(request)
    return redirect('computers_list')
