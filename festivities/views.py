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
from api_responses.responses import Response200, Response201, Response400


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
  Class based view to handle CRUD operations over festivities objects

  ...
  Methods:
      list(): Returns all the festivities in JSON format
      create(): Creates a festivity object
      update(): Allows update a festivity (partial)
  '''

  serializer_class = FestivitySerializer

  def list(self, request):
    '''
    This method returns all festivities and filter festivities by query params

    ...
    Params    
      - name: Name of festivities
      - start_date: Start date of festivities
      - place: Place of festivities
      - start_range and end_range: Dates range of festivities
    '''
    if request.GET:
      if request.GET.get("name"):
        festivities = Festivity.objects.filter(name=request.GET['name'])
      elif request.GET.get("start_date"):
        festivities = Festivity.objects.filter(start_date=request.GET['start_date'])
      elif request.GET.get("place"):
        festivities = Festivity.objects.filter(place=request.GET['place'])
      elif (request.GET.get("start_range")) and (request.GET.get("end_range")):
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

    ...
    Params    
      - name: Name of festivity
      - start_date: Start date of festivity
      - end_date: Start date of festivity
      - place: Place of festivities
    '''
    serialize_data = self.get_serializer(data=request.data)
    if serialize_data.is_valid():
        self.perform_create(serialize_data)
        return Response201('festivity', serialize_data.data, user_message='Festivity created successfuly').get_response()
    else:
        server_info = serialize_data.errors
        return Response400(server_info, user_message='Sorry. Festivity could not be created').get_response()

  def update(self, request, pk=None):
    '''
    This method updates an existing festivities

    ...
    Params
        pk: (int) The festivity unique primary key identifier
    '''
    if pk:
      festivity, error = self.get_instance_or_400(pk)
      if festivity:
        if request.data.get("place"):
          request.data.pop('place')
        serializer = FestivitySerializer(
          festivity, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
          self.perform_update(serializer)
          return Response200('festivity', serializer.data, user_message='Festivity updated successfuly').get_response()
        else:
          server_info = serializer.errors
          return Response400(server_info, user_message='Sorry. Festivity could not be updated').get_response()
      else:
        return Response400(error, user_message='Sorry. Festivity not found').get_response()
    else:
      return Response400(user_message='Sorry. Please send pk of Festivity').get_response()

  def get_instance_or_400(self, pk):
      '''
      This method checks for an existing role object with related
      pk. If not exist then returns a HTTP 400 error

      Params
          pk: (int) The role unique primary key identifier    
      '''
      try:
        festivity = Festivity.objects.get(id=pk)
        return festivity, None
      except Festivity.DoesNotExist:
        server_info = {
            "errorMessage": "Invalid request: Cannot match any object with the received PK"
        }
        return None, server_info