from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import TemplateDoesNotExist
# Import settings in your views.py or any other file
from django.conf import settings
# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CreateUserForm,LoginForm
from .models import UserProfile  # Ensure this is correct based on your project structure


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate,login,logout


            # If user is not found, show error
            
def register(request):
    context = {
        'title': 'Home Page',
        'welcome_message': 'Welcome to our website!'
    }
    if request.method == 'POST':
        form = CreateUserForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            # Check if the username already exists
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                form.add_error('username', 'A user with that username already exists.')
            else:
                form.save()
                 # Redirect to a success page
        else:
            print(form.errors)  # Print errors to the console for debugging
    else:
        form = CreateUserForm()  # Initialize the form for GET request without any data

    return render(request, 'register.html', {'form': form})

def login(request):
    
    form= LoginForm()
    
    if request.method == 'POST':
        form=LoginForm(request,data=request.POST)
        
        if form.is_valid:
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user= authenticate(request,username=username,password=password)
            
            if user is not None:
                
                auth.login(request,user)
                
                return redirect("dashboard")
            
    context = {'LoginForm':form}
                
            
    return render(request,"login.html")

def landing(request):
    return render(request,"landing.html")

def dashboard(request):
    # Fetch the user profile for the logged-in user
   user_profile, created = UserProfile.objects.get_or_create(user=request.user,defaults={
       
       'age': 0,  # Provide a default value for age
        'weight': 0.0,  # Provide a default value for weight
        'goal_weight': 0.0,  # Provide a default value for goal weight
        'gender': 'other',  # Provide a default value for gender
        'activity_level': 'sedentary'
       
       })  # Fetch or create the user profile
   print("Current UserProfile before submission:", user_profile)

   if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=user_profile)  
        
        # Process the form data
        if form.is_valid():
            form.save()  # Save the updated profile
            print("UserProfile after submission:", user_profile)  # Print the profile after saving
            return redirect('dashboard')  # Redirect to the same page or a success page
        else:
            print("Form errors:", form.errors)  # Print errors to the console for debugging
    

    # Fetch and print all UserProfile records to check if the insertion was successful
    
 
        
   return render(request, 'dashboard.html', {'user_profile': user_profile})

def food_item_list(request):
    try:
        return render(request, 'food_item_list.html')
    except TemplateDoesNotExist:
        print("Template search paths:", settings.TEMPLATES)
        raise