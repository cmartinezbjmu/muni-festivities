"""Festivities models."""

# Django
from django.db import models

class Festivity(models.Model):
  '''
  Festivity model store the festivity information.
  ...
  Attributes
        
      name: (str) The festivity name
      start_date: (Date & time) Date to start festivity
      end_date: (Date & time) Date to end festivity
      place: (str) The place where they will be held the celebrate
      createdAt: Date & time filed to store creation date 
      updatedAt: Date & time filed to store last updated date
  '''
  name = models.CharField(max_length=150, blank=False, null=False)
  start_date = models.DateField(null=False, blank=False)
  end_date = models.DateField(null=False, blank=False)
  place = models.CharField(max_length=150, blank=False, null=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'festivities'