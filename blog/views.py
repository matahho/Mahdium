from django.shortcuts import render
from .models import Post
from datetime import datetime

data = [

    {   
        'date_posted':'',
        'title':'Post 1',
        'author':'Mahdi',
        'content':'First Content'
    },
    {
        'date_posted':'',
        'title':'Post 2',
        'author':'Ali',
        'content':'Second Content'
    },
    
]


def home (request):
    currentdate = datetime.now().strftime("%H:%M:%S")
    print ("here" , currentdate)
    return render(request , "blog/home.html" , context={'posts':Post.objects.all() , 'title':'Home' , 'currentTime':currentdate})


def about (request):
    return render(request , "blog/about.html" , )
