from django.shortcuts import render
from .models import Post
from datetime import datetime



def home (request):
    currentdate = datetime.now().strftime("%H:%M:%S")
    return render(request , "blog/home.html" , context={'posts':Post.objects.all() , 'title':'Home' , 'currentTime':currentdate})


def about (request):
    return render(request , "blog/about.html" , )
