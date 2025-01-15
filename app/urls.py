from django.urls import path
from .views import *

urlpatterns = [
    path('register-bootcamp/', register_bootcamp, name='register-bootcamp'),
]
