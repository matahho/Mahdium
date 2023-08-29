from django.shortcuts import render


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
    
    return render(request , "blog/home.html" , context={'posts':data , 'title':'Home'})


def about (request):
    return render(request , "blog/about.html" , )
