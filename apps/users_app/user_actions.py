from .models import User
from django.contrib import messages

class UserActions:
    @classmethod
    def login(cls, request, form):
        email = form.cleaned_data.get('email')
        user = User.objects.get(email=email)
        request.session['userid'] = user.id
        messages.success(request, "Logged In")
    @classmethod
    def register(cls, request, form):
        user = form.save()
        request.session['userid'] = user.id
        messages.success(request, "Registered")