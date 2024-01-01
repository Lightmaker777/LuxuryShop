# core/urls.py
from django.urls import path
from .views import home, user_search, user_profile, follow_unfollow


urlpatterns = [
    path('',home, name='home'),
    path('user_search/', user_search, name='user_search'),
    path('profiles/<username>/', user_profile, name='user_profile'),
    path('follow_unfollow/<username>/', follow_unfollow, name='follow_unfollow'),
]
    
