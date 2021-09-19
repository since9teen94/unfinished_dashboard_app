from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def register_validator(self, rd):
        email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        name_regex = re.compile('[0-9]')
        errors = {}
        if len(rd['password']) < 8 or len(rd['confirm_pw']) < 8:
            errors['password'] = "Password must be at least 8 characters long"
        if rd['password'] != rd['confirm_pw']:
            errors['confirm_pw'] = "Passwords must match"
        if len(rd['first_name']) < 2 or len(rd['last_name']) < 2:
            errors['first_name'] = "First name must be at least two characters"
            errors['last_name'] = "Last name must be at least two characters"
        if not email_regex.match(rd['email']):
            errors['email'] = "Email not valid"
        if User.objects.filter(email=rd['email']):
            errors['email_unique'] = "Email not unique"
        if name_regex.search(rd['first_name']) or name_regex.search(rd['last_name']):
            errors['name_format'] = "Names can not contain numbers"
        return errors
    
    def signin_validator(self, rd):
        errors = {}
        if not User.objects.filter(email=rd['email']):
            errors['email'] = "Email does not exist"
            return errors
        this_user = User.objects.get(email=rd['email'])
        if not bcrypt.checkpw(rd['password'].encode(), this_user.password.encode()):
            errors['password'] = "Password not valid"
        return errors
        
        

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()