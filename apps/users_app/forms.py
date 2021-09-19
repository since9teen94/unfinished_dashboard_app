# from django import forms
# from django.forms import widgets
# from .models import User
# from django.core.exceptions import ValidationError
# import re

# def name_len(value):
#     if len(value) < 2:
#         raise ValidationError("Names must be at least two characters")
# def pw_len(value):
#     if len(value) < 8:
#         raise ValidationError("Password must be at least eight characters")
# def email_format(value):
#     email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#     if not email_regex.match(value):
#         raise ValidationError("Please enter a valid email")
# def email_unique(value):
#     if User.objects.filter(email=value):
#         raise ValidationError("Email already in use")
# def name_format(value):
#     name_regex = re.compile('[0-9]')
#     if name_regex.search(value):
#         raise ValidationError("Name must not have numbers in it")


# class RegistrationForm(forms.Form):
#     first_name = forms.CharField(max_length=255,label='First Name', widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'First Name',}), validators=[name_len, name_format])
#     last_name = forms.CharField(max_length=255,label='Last Name', widget=forms.TextInput(attrs={'class':'form-control mb-3','placeholder':'Last Name',}), validators=[name_len, name_format])
#     email = forms.CharField(max_length=255,label='Email', widget=forms.EmailInput(attrs={'class':'form-control mb-3','placeholder':'Email',}), validators=[email_unique, email_format])
#     password = forms.CharField(max_length=255,label='Password', widget=forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Password',}), validators=[pw_len])
#     confirm_pw = forms.CharField(max_length=255,label='Confirm PW', widget=forms.PasswordInput(attrs={'class':'form-control mb-3','placeholder':'Confirm PW',}), validators=[pw_len])

#     def clean(self):
#         cleaned_data = super(RegistrationForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_pw = cleaned_data.get("confirm_pw")
    
#         if password and confirm_pw and password != confirm_pw:
#             self.add_error('confirm_pw', "Password does not match")
    
#         return cleaned_data