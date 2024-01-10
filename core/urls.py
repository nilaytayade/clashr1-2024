from django.urls import path
from .views import Get_mcq,test
urlpatterns=[
    path('getmcq/',Get_mcq),
]