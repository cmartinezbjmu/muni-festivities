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
    '''
    This method returns all festivities and filter festivities by query params:
      - name: Name of festivities
      - start_date: Start date of festivities
      - place: Place of festivities
      - start_range and end_range: Dates range of festivities
    '''
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
  
  def create(self, request):
    '''
    This method creates a festivity
      - name: Name of festivity
      - start_date: Start date of festivity
      - end_date: Start date of festivity
      - place: Place of festivities
    '''
    serialize_data = self.get_serializer(data=request.data)
    if serialize_data.is_valid():
        self.perform_create(serialize_data)
        return Response200('festivity', serialize_data.data, user_message='Festivity created successfuly').get_response()
    else:
        server_info = serialize_data.errors
        return Response400(server_info, user_message='Sorry. Festivity could not be created').get_response()    