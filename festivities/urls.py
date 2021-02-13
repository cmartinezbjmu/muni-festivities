"""Festivities urls."""

# Django
from django.urls import path

# Views
from .views import check_status, FestivitiesViewSet

urlpatterns = [
  path('festivities/',
        FestivitiesViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='festivities-list'),
  path('festivities/<int:pk>/',
        FestivitiesViewSet.as_view({'patch': 'update'}),
        name='festivities-detail'),
  path('are-you-alive', check_status, name='check-alive'),
]
