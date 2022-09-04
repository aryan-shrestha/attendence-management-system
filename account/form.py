from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(label='Password', max_length=100, widget= forms.PasswordInput (attrs={'class': "form-control"}))
    password2 = forms.CharField(label="Password Confirmation", max_length=100, widget=forms.PasswordInput(attrs={'class': "form-control"}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                    'email', 'password1', 'password2']

class MyUserUpdateForm(forms.ModelForm):

    first_name = forms.CharField(label='First Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Last Name', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Email Address', max_length=100, widget=forms.EmailInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                    'email']
