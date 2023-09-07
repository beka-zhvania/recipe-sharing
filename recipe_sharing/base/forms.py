from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


form_styling = 'w-full py-4 px-6 rounded-xl text-black'

class CustomRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(
        max_length="50",
        required=True,
        help_text='Please enter a valid username',
        widget=forms.TextInput(attrs={
        'placeholder': "Your username",
        'class': form_styling
        })
    )

    email = forms.EmailField(
        max_length=100, 
        required=True, 
        help_text='Please enter a valid email address.', 
        widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address...',
        'class': form_styling
        })
    )

    password1 = forms.CharField(
        max_length="50",
        required=True,
        help_text='Please enter a password',
        widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': form_styling
    })
    )

    password2 = forms.CharField(
        max_length="50",
        required=True,
        help_text='Please repeat the password',
        widget=forms.PasswordInput(attrs={
        'placeholder': "Your password",
        'class': form_styling
        })
    )