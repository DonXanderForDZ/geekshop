from atexit import register
from datetime import datetime
import datetime
from django import template

register = template.Library()

@register.simple.tag
def current_year():
    return datetime.datetime.now().year