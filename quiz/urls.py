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
   
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    

]