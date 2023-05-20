from django import template
from ..models import AboutUs

register = template.Library()

def about():
    about = AboutUs.objects.all()
    return about