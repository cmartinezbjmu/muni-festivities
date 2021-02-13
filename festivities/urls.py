"""Festivities urls."""

# Django
from django.urls import path

# Views
from .views import check_status, FestivitiesViewSet

urlpatterns = [
  path('festivities/',
        FestivitiesViewSet.as_view({'get': 'list'}),
        name='festivities-list'),
  path("are-you-alive", check_status, name="check-alive"),        
]