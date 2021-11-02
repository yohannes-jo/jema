from django.urls import path, include

from .views import register, profileRegistration

app_name = 'profiles'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('new_profile', profileRegistration, name='new_profile'),
]