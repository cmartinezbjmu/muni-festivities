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
        reverse("festivities-detail"), formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["name"], "Juan Fers Birthday")
    self.assertEqual(response.status_code, 200)

  def test_festivities_list_by_queryparam_name(self):
    """Valid test to retrieve all festivities filtered by queryparam name."""

    response = self.client.get(
        reverse("festivities-detail"), {"name": "Christmas"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["start_date"], "2021-12-24")
    self.assertEqual(response.status_code, 200)

  def test_festivities_list_by_queryparam_start_date(self):
    """Valid test to retrieve all festivities filtered by queryparam start_date."""

    response = self.client.get(
        reverse("festivities-detail"), {"start_date": "2021-12-24"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["place"], "House")
    self.assertEqual(response.status_code, 200)     

  def test_festivities_list_by_queryparam_place(self):
    """Valid test to retrieve all festivities filtered by queryparam place."""

    response = self.client.get(
        reverse("festivities-detail"), {"place": "Park"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["name"], "Juan Fers Birthday")
    self.assertEqual(response.status_code, 200)         

  def test_festivities_list_by_queryparam_date_range(self):
    """Valid test to retrieve all festivities filtered by queryparams start_range and end_range."""

    response = self.client.get(
        reverse("festivities-detail"), {"start_range": "2021-02-10", "end_range": "2021-02-15"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["place"], "Park")
    self.assertEqual(response.status_code, 200)

  def test_invalit_festivities_list_by_wrong_queryparam(self):
    """Invalid test to retrieve all festivities filtered by wrong queryparam."""

    response = self.client.get(
        reverse("festivities-detail"), {"range": "2021-02-10"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["user_message"], "Sorry, please check queryparams.")
    self.assertEqual(response.status_code, 400)    