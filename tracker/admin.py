from django.contrib import admin
   # admin.py
from django.contrib import admin
from .models import UserProfile  # Import your model
admin.site.register(UserProfile)  # Register the model with the admin site
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'weight', 'goal_weight', 'gender', 'activity_level')  # Fields to display in the list view
    search_fields = ('user__username',)  # Enable search by username