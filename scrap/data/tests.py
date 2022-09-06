
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import *


class CreateuserTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='pratik', email='sphoeni@gamil.com', password='pass@234',
                                             first_name='pratik', last_name='chakane')
        self.position=Position.objects.create(position='OH')


    def test_login_validuser(self):
        """test case for login valid user"""
        user = User.objects.get(id=1)
        self.client.force_authenticate(user=user)
        response = self.client.post(reverse('data:login'), {"username": "pratik", "password": "pass@234"}, )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

