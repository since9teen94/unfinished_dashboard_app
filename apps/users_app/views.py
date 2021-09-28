from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from .forms import LoginForm, RegistrationForm
from datetime import date

# Create your views here.
def index(request):
    if 'userid' in request.session:
        today = date.today()
        return render(request, 'success.html', {'date':today})
    return render(request, 'index.html')

def signin(request):
    log_form = LoginForm()
    if request.method == 'POST':
        log_form = LoginForm(request.POST)
        if log_form.is_valid():
            email = log_form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            request.session['userid'] = user.id
            messages.success(request, "Logged In")
            return redirect('users:success')
    return render(request, 'signin.html', {'log_form':log_form})

def register(request):
    reg_form = RegistrationForm()
    if request.method == 'POST':
        reg_form = RegistrationForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            request.session['userid'] = user.id
            messages.success(request, "Registered")
            return redirect('users:success')
    return render(request, 'register.html', {'reg_form':reg_form})

def success(request):
    return redirect('users:index')

def logout(request):
    if 'userid' in request.session:
        request.session.flush()
    return redirect('users:index')