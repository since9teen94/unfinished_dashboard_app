from django.core.exceptions import ValidationError
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile('[0-9]')

def first_name_len(value):
    if len(value) < 2:
        raise ValidationError("First name must be at least two characters")
def last_name_len(value):
    if len(value) < 2:
        raise ValidationError("Last name must be at least two characters")
def pw_len(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least eight characters")
def confirm_pw_len(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least eight characters")
def email_format(value):
    if not email_regex.match(value):
        raise ValidationError("Please enter a valid email")
def first_name_format(value):
    if name_regex.search(value):
        raise ValidationError("Name must not have numbers in it")
def last_name_format(value):
    if name_regex.search(value):
        raise ValidationError("Name must not have numbers in it")