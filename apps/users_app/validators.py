from django.core.exceptions import ValidationError
import re

def name_len(value):
    if len(value) < 2:
        raise ValidationError("Names must be at least two characters")
def pw_len(value):
    if len(value) < 8:
        raise ValidationError("Password must be at least eight characters")
def email_format(value):
    email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not email_regex.match(value):
        raise ValidationError("Please enter a valid email")
def name_format(value):
    name_regex = re.compile('[0-9]')
    if name_regex.search(value):
        raise ValidationError("Name must not have numbers in it")