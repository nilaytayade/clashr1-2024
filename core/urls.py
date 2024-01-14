from django.urls import path
from .views import get_mcq,get_leaderboard,submit

# urls.py
from django.urls import path
from .views import RegistrationView, LoginView


urlpatterns=[
    path('getmcq/',get_mcq),
    path('getleaderboard/',get_leaderboard),
    path('submit/',submit),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
]