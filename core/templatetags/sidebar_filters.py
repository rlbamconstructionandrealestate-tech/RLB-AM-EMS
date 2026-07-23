# templatetags/sidebar_filters.py
from django import template

register = template.Library()

@register.filter(name='startswith')
def startswith(value, arg):
    """Returns True if the value starts with the argument"""
    if value is None or arg is None:
        return False
    return str(value).startswith(str(arg))