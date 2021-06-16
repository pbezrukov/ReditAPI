from django.urls import re_path

from .views import RegistrationAPIView
# from .views import LoginAPIView
from django.urls import path

urlpatterns = [
    path("registration", RegistrationAPIView.as_view(), name='user_registration'),
]
