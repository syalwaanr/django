from django import template
from django.utils.html import strip_tags
from django.utils.text import Truncator
from html import unescape

register = template.Library()

@register.filter(name='truncatechars_html')
def truncatechars_html(value, arg):
    if value:
        plain = strip_tags(unescape(value))
        return Truncator(plain).chars(arg, truncate='...')
    return ''
