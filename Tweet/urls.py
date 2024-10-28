from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tweet_list/', views.Tweet_list, name='tweet_list'),
    path('create/', views.Tweet_create, name='Tweet_create'),  # Add this line
    path('<int:tweet_id>/edit/', views.Edit_tweet, name='Edit_tweet'),
    path('<int:tweet_id>/delete/', views.Delete_tweet, name='Delete_tweet'),
]
