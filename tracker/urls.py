from django.urls import path
from . import views

urlpatterns = [
     path('', views.landing, name='landing'),  #
    path('landing/',views.landing,name='landing_alt'),

    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('food-item-list/', views.food_item_list, name='food_item_list'),  # New URL for food item list
]

