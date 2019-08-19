from django import forms
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField(widget=forms.Textarea())
    birth_date = forms.CharField(widget=forms.DateInput())

class SignInForm(AuthenticationForm):
   username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
   password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
