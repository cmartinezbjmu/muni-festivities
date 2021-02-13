"""Responses module to handle default service responses."""

from django.http import JsonResponse
import rest_framework.status as status_codes


class Response200:
  """The Response200 class allows to create
  objects to returns HTTP 200 responses
  """

  def __init__(self, attr, data, server_info=None, user_message=""):
    self.attr = attr
    self.data = data
    self.server_info = server_info if server_info is not None else {}
    self.user_message = user_message
    self.status_code = status_codes.HTTP_200_OK

  def get_response(self):
    if self.data:
      data = {"{}".format(self.attr): self.data}
    else:
      data = {}
    response = {
        "data": data,
        "server_info": self.server_info,
        "user_message": self.user_message,
    }
    return JsonResponse(response, status=self.status_code)


class Response400:
  """The Response400 class allows to create
  objects to returns HTTP 400 responses
  """

  def __init__(self, server_info=None, user_message=""):
    self.server_info = server_info if server_info is not None else {}
    self.user_message = user_message
    self.status_code = status_codes.HTTP_400_BAD_REQUEST

  def get_response(self):
    data = {}
    response = {
        "data": data,
        "server_info": self.server_info,
        "user_message": self.user_message,
    }
    return JsonResponse(response, status=self.status_code)
