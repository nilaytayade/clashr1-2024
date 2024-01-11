from django.urls import path
from .views import get_mcq,get_leaderboard,submit
urlpatterns=[
    path('getmcq/',get_mcq),
    path('getleaderboard/',get_leaderboard),
    path('submit/',submit),
    
]