from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('explore/', views.explore, name='explore'),
    path('notifications/<str:username>', views.notification, name='notification')
]