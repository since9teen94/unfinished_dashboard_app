from django.shortcuts import render, redirect

from apps.users_app.models import Message
from .forms import LoginForm, RegistrationForm, MessageForm
from .user_actions import UserActions

# Create your views here.
def index(request):
    if 'userid' in request.session:
        msg_form = MessageForm()
        posts =Message.objects.all()
        recents = Message.objects.all().order_by('-created_at')[:3]
        return render(request, 'success.html', {'msg_form':msg_form, 'posts':posts, 'recents':recents, 'user':UserActions.get_user(request)})
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

def post_message(request):
    msg_form = MessageForm(request.POST or None)
    if msg_form.is_valid():
        UserActions.post_message(request, msg_form)
        return redirect('users:success')
    return render(request, 'index.html', {'msg_form':msg_form})

def delete_message(request):
    if 'userid' in request.session:
        msg_id = request.args.get('msg_id')
        this_msg = Message.objects.get(id=msg_id)
    return redirect('users:index')
def edit_message(request):
    if 'userid' in request.session:
        pass
        # msg_id = request.args.get('msg_id')
        # this_msg = Message.objects.get(id=msg_id)
    return redirect('users:index')
def comment_message(request):
    if 'userid' in request.session:
        pass
        # msg_id = request.args.get('msg_id')
        # this_msg = Message.objects.get(id=msg_id)
    return redirect('users:index')

def user_page(request):
    if 'userid' in request.session:
        return render(request, 'user_page.html', {'user':UserActions.get_user(request)})
    return redirect('users:index')