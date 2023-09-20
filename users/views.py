from django.shortcuts import render , redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register (request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request , f"Welcome {username}, Your account created !")
            return redirect('blog-home')
        else:
            for field, error in form.errors.items():
                messages.warning(request , error[0])
            

    else :
        form = UserRegisterForm()
    
    return render(request , 'users/register.html' , {'form':form} )
