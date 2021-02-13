"""Festivities views."""

# Django

# Django Rest Framework
from rest_framework import viewsets
from rest_framework.decorators import api_view

# Models

# Serializers

# Response
from api_responses.responses import Response200, Response400

@api_view(["GET"])
def check_status(request):
  """
    Simple view function to check the API status
    Args:
        request (object): The request object
    """
  return Response200("status", "Ok", user_message="API working").get_response()