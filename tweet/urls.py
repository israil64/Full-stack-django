from django.urls import path
from .import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tweet_list/', views.tweet_list, name='tweet_list'),
    path('tweet_create/', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('register/', views.register, name='register'),
    path('search_tweet/', views.search_tweet, name='search_tweet'),
    path('user_login/', views.user_login, name='user_login'),

]



