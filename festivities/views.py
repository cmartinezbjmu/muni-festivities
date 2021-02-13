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
    if request.GET:
      if 'name' in request.GET:
        festivities = Festivity.objects.filter(name=request.GET['name'])
      elif 'start_date' in request.GET:
        festivities = Festivity.objects.filter(start_date=request.GET['start_date'])
      elif 'place' in request.GET:
        festivities = Festivity.objects.filter(place=request.GET['place'])
      elif ('start_range' in request.GET) and ('end_range' in request.GET):
        festivities = Festivity.objects.filter(start_date__range=[request.GET['start_range'], request.GET['end_range']])
      else:
        return Response400(user_message='Sorry, please check queryparams.').get_response()    
    else:
      festivities = Festivity.objects.all()
    serializer = FestivitySerializer(festivities, many=True)
    return Response200('festivities',
                        serializer.data,
                        user_message='Success.').get_response()