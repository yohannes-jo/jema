from django.urls import path, include

from .views import register, profile_registration, my_profile, edit_profile

app_name = 'profiles'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('new_profile/', profile_registration, name='new_profile'),
    path('<str:username>/', my_profile, name='my_profile'),
    path('edit_profile/<str:username>/', edit_profile, name='edit_profile'),
]