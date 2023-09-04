from django.urls import path
from . import views

app_name = 'queans'

urlpatterns = [
   
    path('',views.home , name = 'home'),

    path('create_question/',views.create_question,name='create_question'),
    path('create_answer/',views.create_answers,name='create_answer'),

    
]
