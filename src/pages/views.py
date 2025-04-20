from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Me</h1>")

def about_view(*args,**kwargs):
    return HttpResponse("<h1>About Us</h1>")