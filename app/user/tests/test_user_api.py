from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse('user:create')

def create_user (**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """test creating user with valid payload is successful"""
        payload = {
            'username': 'ali',
            'password': '123'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        print('res:' + str(res.data))
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        # self.assertNotIn('password', res.data)

    def test_user_exists(self):
        """test creating user that already exists falis"""
        payload = {
            'username': 'ali',
            'password': '123'
        }
        create_user(**payload)  

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    

