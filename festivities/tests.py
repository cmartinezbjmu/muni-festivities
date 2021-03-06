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
    Festivity.objects.create(
      name="Juan Fers Birthday", start_date="2021-02-13 20:40:26.744511-05",
      end_date="2021-02-13 00:40:26.744511-05", place="Park"
    )
    Festivity.objects.create(
      name="Christmas", start_date="2021-12-24 00:40:26.00000-00",
      end_date="2021-12-25 00:40:26.744511-05", place="House"
    )

  def test_festivities_list(self):
    """Valid test to retrieve all festivities."""

    response = self.client.get(
      reverse("festivities-list"), formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["name"],
      "Juan Fers Birthday")
    self.assertEqual(response.status_code, 200)

  def test_festivities_list_by_queryparam_name(self):
    """Valid test to retrieve all festivities filtered by queryparam name."""

    response = self.client.get(
      reverse("festivities-list"), {"name": "Christmas"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["place"],
      "House")
    self.assertEqual(response.status_code, 200)

  def test_festivities_list_by_queryparam_start_date(self):
    """Valid test to retrieve festivities filtered by queryparams start_date"""

    response = self.client.get(
      reverse("festivities-list"), {"start_date": "2021-02-13 20:40:26.744511-05"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["place"], "Park")
    self.assertEqual(response.status_code, 200)

  def test_festivities_list_by_queryparam_place(self):
    """Valid test to retrieve all festivities filtered by queryparam place."""

    response = self.client.get(
      reverse("festivities-list"), {"place": "Park"}, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["name"],
      "Juan Fers Birthday")
    self.assertEqual(response.status_code, 200)

  def test_festivities_list_by_queryparam_date_range(self):
    """
    Valid test to retrieve all festivities filtered by queryparams
    start_range and end_range.
    """

    response = self.client.get(
      reverse("festivities-list"),
        {"start_range": "2021-02-10", "end_range": "2021-02-15"},
        formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivities"][0]["place"], "Park")
    self.assertEqual(response.status_code, 200)

  def test_invalit_festivities_list_by_wrong_queryparam(self):
    """Invalid test to retrieve all festivities filtered by wrong queryparam."""

    response = self.client.get(
      reverse("festivities-list"), {"range": "2021-02-10"},
      formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["user_message"],
      "Sorry, please check queryparams.")
    self.assertEqual(response.status_code, 400)

  def test_festivities_create(self):
    """Valid test to create a festivity."""

    response = self.client.post(
      reverse("festivities-list"), {
        "name": "New event",
        "start_date": "2021-05-13 00:40:26.744511-05",
        "end_date": "2021-05-20 00:40:26.744511-05",
        "place": "Stadium"
      }, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivity"]["place"], "Stadium")
    self.assertEqual(response.status_code, 201)

  def test_invalid_festivities_create(self):
    """Invalid test to create a festivity."""

    response = self.client.post(
      reverse("festivities-list"), {
        "name": "New event",
        "start_date": "2021-05-13 00:40:26.744511-05",
        "end_date": "2021-05-20 00:40:26.744511-05"
      }, formal="json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["server_info"],
      {"place": ["Este campo es requerido."]})
    self.assertEqual(response.status_code, 400)

  def test_festivities_update(self):
    """Valid test to update a festivity."""

    response = self.client.patch(
      reverse("festivities-detail", kwargs={"pk": 1}),
        {"name": "Update Name", "place": "none"},
        content_type="application/json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["data"]["festivity"]["name"], "Update Name")
    self.assertEqual(response_data["data"]["festivity"]["place"], "Park")
    self.assertEqual(response.status_code, 200)

  def test_invalid_festivities_update(self):
    """Invalid test to update a festivity."""

    response = self.client.patch(
      reverse("festivities-detail", kwargs={"pk": 10}),
        {"name": "Update Name"}, content_type="application/json"
    )
    response_data = json.loads(response.content)
    self.assertEqual(response_data["user_message"],
      "Sorry. Festivity not found")
    self.assertEqual(response.status_code, 400)
  