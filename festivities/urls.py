"""Festivities urls."""

# Django
from django.urls import path

# Views
from .views import check_status


urlpatterns = [
  path("are-you-alive", check_status, name="check-alive"),
]