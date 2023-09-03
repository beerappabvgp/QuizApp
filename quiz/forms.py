from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUsercreationForm(UserCreationForm):
    is_creator = forms.CheckboxInput()
    class Meta:
        model = CustomUser
        fields = ['username' , 'email' , 'password1' , 'password2' , 'is_creator']

class PasswordResetForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'placeholder' : 'Enter your email'})
    )


