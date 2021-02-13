"""Festivities views."""

# Django

# Django Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

# Models
from .models import Festivity

# Serializers
from .serializers import FestivitySerializer

# Response
from api_responses.responses import Response200, Response400


@api_view(["GET"])
def check_status(request):
  """
  Simple view function to check the API status
  Args:
      request (object): The request object
  """
  return Response200("status", "Ok",
                      user_message="API working").get_response()


class FestivitiesViewSet(ModelViewSet):
  '''
  Class based view to handle CRUD operations over festities objects

  ...
  Methods:
      list(): Returns all the festivities in JSON format
      retrieve(): Retrieve a specific festivity in JSON format
      create(): Creates a festivity object
      update(): Allows update a festivity (partial and full)
  '''

  serializer_class = FestivitySerializer

  def list(self, request):
    festivities = Festivity.objects.all()
    serializer = FestivitySerializer(festivities, many=True)
    return Response200('festivities',
                        serializer.data,
                        user_message='Success.').get_response()
