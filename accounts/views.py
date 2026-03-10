"""
Interface layer (Views) for the Accounts module.

Handles user registration, login, logout, and account-related UI.
"""

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.hashers import make_password
from django.utils.crypto import get_random_string
from .models import User, Student

def info_account(request):
    """
    Renders the simplified registration page.
    """
    return render(request, 'accounts/register.html')

def account_selection(request):
    """
    Renders the account selection/info page.
    """
    return render(request, 'accounts/info_account.html')

def account_store(request):
    """
    Handles student registration and automatic login.

    This matches legacy Laravel logic where students are registered and
    immediately logged in without a manual password entry in the first step.
    """
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = User.objects.filter(email=email).first()
        if not user:
            full_name = f"{first_name} {last_name}"
            # Use a secure random password for new student accounts
            # since they don't provide one in this specific flow.
            user = User.objects.create_user(
                email=email,
                full_name=full_name,
                password=get_random_string(12),
                role='student'
            )
            Student.objects.create(user=user)

        auth_login(request, user)
        request.session['role'] = user.role
        request.session['name'] = user.full_name

        return redirect('testing:test_instructions')
    return redirect('accounts:info_account')

def user_login(request):
    """
    Handles standard user authentication and redirection based on role.
    """
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user:
            auth_login(request, user)
            request.session['role'] = user.role
            request.session['name'] = user.full_name

            if user.role == 'admin': return redirect('classroom:developer_dashboard')
            if user.role == 'teacher': return redirect('classroom:teacher_dashboard')
            return redirect('core:index')
        else:
            return render(request, 'accounts/login.html', {'login_error': 'البريد الإلكتروني أو كلمة المرور غير صحيحة.'})
    return render(request, 'accounts/login.html')

def logout(request):
    """
    Logs out the current user and redirects to the index page.
    """
    auth_logout(request)
    return redirect('core:index')
