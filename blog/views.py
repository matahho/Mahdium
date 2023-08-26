from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home (request):
    return HttpResponse("<h1>Home blog</h1>")


def about (request):
    return HttpResponse("<h1>ABout us</h1>")
