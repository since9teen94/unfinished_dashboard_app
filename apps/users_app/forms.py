from django import forms
from django.forms import widgets
from .models import User
from django.core.exceptions import ValidationError
from .validators import first_name_len,first_name_format,last_name_len,last_name_format,email_format,pw_len,confirm_pw_len
import re
import bcrypt

class UserFormMixin(forms.ModelForm):
    first_name = forms.CharField(max_length=255,label='First Name', widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'First Name','id':'first_name'}), validators=[first_name_len, first_name_format])
    last_name = forms.CharField(max_length=255,label='Last Name', widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Last Name',}), validators=[last_name_len, last_name_format])
    email = forms.CharField(max_length=255,label='Email', widget=forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Email',}), validators=[email_format])
    password = forms.CharField(max_length=255,label='Password', widget=forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Password',}), validators=[pw_len])

class RegistrationForm(UserFormMixin):
    confirm_pw = forms.CharField(max_length=255,label='Confirm PW', widget=forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Confirm PW',}), validators=[confirm_pw_len])
    class Meta:
        model = User
        fields = ('first_name','last_name','email','password','confirm_pw')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get("password")
        confirm_pw = cleaned_data.get("confirm_pw")
        email = cleaned_data.get('email')
    
        if User.objects.filter(email=email):
            self.add_error('email', 'Email already in use')
        if password and confirm_pw and password != confirm_pw:
            self.add_error('password', "Password does not match")
        return cleaned_data
    # hashes a password upon creation of a new user, i.e. successful registration
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.password = bcrypt.hashpw(self.cleaned_data["password"].encode(), bcrypt.gensalt()).decode()
        if commit:
            user.save()
        return user

class LoginForm(UserFormMixin):

    first_name = None
    last_name = None

    class Meta:
        model = User
        fields = ('email','password')

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not User.objects.filter(email=email):
            self.add_error('email','Invalid Credentials')
            return cleaned_data
        this_user = User.objects.get(email=email)
        if not bcrypt.checkpw(password.encode(), this_user.password.encode()):
            self.add_error('password','Invalid Credentials')
        return cleaned_data