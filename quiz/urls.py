from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



app_name = 'quiz'

urlpatterns = [
    path('',views.home , name = "home"),
    path('register/',views.register , name = 'register'),
    path('login/',views.user_login , name='login'),
    path('dashboard/',views.dashboard , name = 'dashboard'),
    path('logout/',auth_views.LogoutView.as_view() , name = 'logout'),
]