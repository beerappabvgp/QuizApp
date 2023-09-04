from django.contrib import messages
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse
from .forms import  QuestionForm,AnswerForm

# def create_quiz(request):
#     if request.method == 'POST':
#         form = QuizForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request,'Quiz is created successfully')
#             return redirect('queans:create_question')

#     else:
#         form = QuizForm()

#     return render(request , 'queans/create_quiz.html',{'form' : form})


def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Quiz is created successfully')
            return redirect('queans:home')

    else:
        form = QuestionForm()

    return render(request , 'queans/create_question.html',{'form' : form})


def home(request):
    return HttpResponse("Queans")

def create_answers(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Quiz is created successfully')
            return redirect('queans:home')

    else:
        form = AnswerForm()

    return render(request , 'queans/answer_form.html',{'form' : form})

# def create_list(request):
#     if request.method == 'POST':
#         form = QuizListForm(request.POST)

#         if form.is_valid():
#             form.save()
#             messages.success(request,'Quiz is created successfully')
#             return redirect('queans:home')

#     else:
#         form = QuizListForm()

#     return render(request , 'queans/quiz_list.html',{'form' : form})