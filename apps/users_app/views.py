from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from datetime import date
from .user_actions import UserActions


# Create your views here.
def index(request):
    if 'userid' in request.session:
        today = date.today()
        return render(request, 'success.html', {'date':today})
    return render(request, 'index.html')

def signin(request):
    log_form = LoginForm(request.POST or None)
    if log_form.is_valid():
        UserActions.login(request, log_form)
        return redirect('users:success')
    return render(request, 'signin.html', {'log_form':log_form})

def register(request):
    reg_form = RegistrationForm(request.POST or None)
    if reg_form.is_valid():
        UserActions.register(request, reg_form)
        return redirect('users:success')
    return render(request, 'register.html', {'reg_form':reg_form})

def success(request):
    return redirect('users:index')

def logout(request):
    if 'userid' in request.session:
        request.session.flush()
    return redirect('users:index')