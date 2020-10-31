from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTest(TestCase):
    def test_create_user_with_username_successful(self):
        username = "testuser1"
        password = "123"
        user = get_user_model().objects.create_user(
            username = username,
            password = password
        )
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))


    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            username='admin',
            password='admin123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)