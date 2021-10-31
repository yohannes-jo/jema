from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.FeedPage.as_view(), name='index'),
]