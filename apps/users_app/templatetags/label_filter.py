from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def label_format(value):
    return value.replace('_', ' ')