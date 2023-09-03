from django.shortcuts import redirect, render
from .forms import CustomUsercreationForm
from django.contrib.auth import login,authenticate
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


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username , password = password)

        if user is not None:
            login(request, user)
            return redirect('quiz:dashboard')
        else:
            messages.error(request,'Invalid username or password . Please try again .')

    return render(request,'quiz/login.html')


def dashboard(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request,'quiz/dashboard.html',context)


