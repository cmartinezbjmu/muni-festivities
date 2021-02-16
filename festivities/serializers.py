"""Festivities serializers."""

# Django Rest Framework
from rest_framework import serializers

# Models
from .models import Festivity

class FestivitySerializer(serializers.ModelSerializer):
  """
  FestivitySerializer allows rest_framework modules validate
  incoming data for create festivity object. Deliver the
  serialized model also.
  """

  class Meta:
    """Serializer settings."""
    model = Festivity
    fields = ["id", "name", "start_date", "end_date", "place"]
