from django.urls import path, include

from .views import register, profile_registration, detail, edit_profile, follow

app_name = 'profiles'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('new_profile/', profile_registration, name='new_profile'),
    path('<str:username>/', detail, name='detail'),
    path('edit_profile/<str:username>/', edit_profile, name='edit_profile'),
    path('<str:username>/follow/', follow, name='follow')
]