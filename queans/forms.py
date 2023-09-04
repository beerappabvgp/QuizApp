from django import forms
from .models import *

# class QuizForm(forms.ModelForm):
#     class Meta:
#         model = Quiz
#         fields = ['title','description']
    

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text',]
    

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['question','text','is_correct']
    
# class QuizListForm(forms.ModelForm):
#     class Meta:
#         model = QuizList
#         fields = ['questions',]
    

