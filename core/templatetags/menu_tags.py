from django import template
from django.urls import reverse, NoReverseMatch


register = template.Library()



@register.simple_tag
def safe_url(url_name):
    """
    Safely resolves menu URLs.
    Returns # if URL does not exist.
    """

    try:

        return reverse(url_name)

    except NoReverseMatch:

        return "#"