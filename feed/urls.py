from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('add_post/', views.add_post, name='add_post'),
    path('explore/', views.explore, name='explore'),
    path('like/<int:post_id>/', views.like, name='like'),
    path('share/<int:post_id>/', views.share, name='share'),
]