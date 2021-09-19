from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        errors = User.objects.signin_validator(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            return render(request, 'signin.html', {'errors':errors})
        this_user = User.objects.get(email=request.POST['email'])
        request.session['userid'] = this_user.id
        return redirect('users:success')
    return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, val in errors.items():
                messages.error(request, val)
            return render(request, 'register.html', {'errors':errors})
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = pw_hash,
        )
        request.session['userid'] = new_user.id
        return redirect('users:success')
    return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')