from django.db import models
from django.contrib.auth.models import User

# forms.py
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   age = models.IntegerField(null=True )  # Ensure this is set to not allow null values
   weight = models.FloatField(null=False)
   goal_weight = models.FloatField(null=False)
   gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
   activity_level = models.CharField(max_length=20, choices=[('sedentary', 'Sedentary'), ('active', 'Active'), ('very_active', 'Very Active')])

   def __str__(self):
        return self.user.username  # Return the username for easy identification

# forms.py (if you want to keep forms in a separate file)
from django import forms

class CreateUserForm(forms.ModelForm):
    confirmpassword = forms.CharField(widget=forms.PasswordInput)  # Add custom field
    
    class Meta:
        model = User  # Use the User model
        fields = ['username', 'email', 'password', 'confirmpassword']  # Specify the fields to include in the form

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # You can add custom validation for the password here if needed
        return password
