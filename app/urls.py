from django.urls import path
from .views import BootcampRegistrationView

urlpatterns = [
    path('register-bootcamp/', BootcampRegistrationView.as_view(), name='register-bootcamp'),
]
