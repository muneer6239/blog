from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, help_text="Please enter username under 20 characters")
    email = forms.EmailField(label="Email id")
    password1 = forms.CharField(max_length=25, label="Enter Password", widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=25, label="Confirm Password", widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password1']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)

    fields = ['username', 'password']
