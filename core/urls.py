# urls.py
from django.urls import path
from .views import get_mcq, get_leaderboard, submit, UserRegistrationView, SecureEndpoint, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('getmcq/', get_mcq),
    path('getleaderboard/', get_leaderboard),
    path('submit/', submit),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('secure/', SecureEndpoint.as_view(), name='secure-endpoint'),
]
