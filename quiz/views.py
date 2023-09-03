from django.shortcuts import redirect, render
from .forms import CustomUsercreationForm
from django.contrib.auth import login
from django.contrib import messages


def home(request):
    return render(request , 'quiz/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUsercreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login(request,user)
            messages.success(request,"User Created Successfully")
            print("logged")
            return redirect('quiz:home')
    else:
        form = CustomUsercreationForm()

    return render(request,'quiz/register.html' , {'form' : form})
