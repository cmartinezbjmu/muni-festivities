"""Festivities test cases."""

# Django
from django.test import TestCase
from django.urls import reverse

# Models
from .models import Festivity

# Utils
import json

class FestivityTestCase(TestCase):
  """Festivities test cases."""

  @classmethod
  def setUpTestData(cls):
    Festivity.objects.create(name="Juan Fers Birthday", start_date="2021-02-13", end_date="2021-02-13", place="Park")
    Festivity.objects.create(name="Christmas", start_date="2021-12-24", end_date="2021-12-25", place="House")

  def test_festivities_list(self):
    """Valid test to retrieve all festivities."""

    response = self.client.get(
        reverse("festivities-list"), formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["name"], "Juan Fers Birthday")
    self.assertEqual(response.status_code, 200)