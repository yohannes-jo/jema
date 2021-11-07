from django.urls import path

from .import views

app_name = 'notifications'

urlpatterns = [
    path('index/', views.notification, name="index"),
]