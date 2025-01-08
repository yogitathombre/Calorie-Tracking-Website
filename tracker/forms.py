from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput

class CreateUserForm(forms.ModelForm):
     password = forms.CharField(widget=forms.PasswordInput(), label="Create a password")
     confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")
 
     class Meta:
        model= User
        fields =['username','email','password','confirm_password']
        
     def clean_password(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data  # Return cleaned data for further processing
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password=forms.CharField(widget=PasswordInput())
    
    