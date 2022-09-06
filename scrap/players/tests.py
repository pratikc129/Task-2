from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import *


class CreateuserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='pratik', email='sphoeni@gamil.com', password='pass@234',
                                             first_name='pratik', last_name='chakane')
        self.client.login(username="pratik", password="pass@234")
        self.year = Year.objects.create(name='2023')
        self.position = Position.objects.create(position="CB")
        self.highschool = HighSchool.objects.create(name='stv')
        self.country = Country.objects.create(name="India")
        # self.state=State.objects.create(name='Maharashtra',country_id=2)

    def test_year_read(self):
        year = Year.objects.get(name='2023')
        response = self.client.get(reverse('players:yearapi2', args=[year.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_year_delete(self):
        year = Year.objects.get(name='2023')
        response = self.client.delete(reverse('players:yearapi2', args=[year.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_year_update(self):
        update_data = {"name": "2022"}
        year = Year.objects.get(name='2023')
        response = self.client.patch(reverse('players:yearapi2', args=[year.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_position_read(self):
        pos = Position.objects.get(position='CB')
        response = self.client.get(reverse('players:positionapi2', args=[pos.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_position_delete(self):
        pos = Position.objects.get(position='CB')
        response = self.client.delete(reverse('players:positionapi2', args=[pos.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_position_update(self):
        update_data = {"position": "AS"}
        pos = Position.objects.get(position='CB')
        response = self.client.patch(reverse('players:positionapi2', args=[pos.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_highschool_read(self):
        school = HighSchool.objects.get(name='stv')
        response = self.client.get(reverse('players:highschoolapi2', args=[school.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_highschool_delete(self):
        school = HighSchool.objects.get(name='stv')
        response = self.client.delete(reverse('players:highschoolapi2', args=[school.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_highschool_update(self):
        update_data = {"name": "sjv"}
        school = HighSchool.objects.get(name='stv')
        response = self.client.patch(reverse('players:highschoolapi2', args=[school.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_read(self):
        school = Country.objects.get(name='India')
        response = self.client.get(reverse('players:countryapi2', args=[school.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_country_delete(self):
        school = Country.objects.get(name='India')
        response = self.client.delete(reverse('players:countryapi2', args=[school.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_country_update(self):
        update_data = {"name": "Uk"}
        school = Country.objects.get(name='India')
        response = self.client.patch(reverse('players:countryapi2', args=[school.id]), update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

