from django.urls import path
from .views import get_mcq,get_leaderboard,submit,MyTokenObtainPairView

from rest_framework_simplejwt.views import (
   
    TokenRefreshView,
)

urlpatterns=[
    path('getmcq/',get_mcq),
    path('getleaderboard/',get_leaderboard),
    path('submit/',submit),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]