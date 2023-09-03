from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('',views.home , name = "home"),
    path('register/',views.register , name = 'register'),
    path('login/',views.user_login , name='login'),
    path('dashboard/',views.dashboard , name = 'dashboard'),
]