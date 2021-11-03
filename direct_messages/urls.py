from django.urls import path

from . import views

app_name = 'direct_messages'

urlpatterns = [
    path('', views.messages, name='inbox'),
    path('send_message/', views.send_message, name='send_message'),
]