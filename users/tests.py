from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()


class UserModelTests(TestCase):

    def test_create_user(self):

        user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='password123'
        )

        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')

        self.assertTrue(
            user.check_password('password123')
        )

    def test_create_superuser(self):

        admin = User.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            password='admin123'
        )

        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_email_is_unique(self):

        User.objects.create_user(
            email='test@example.com',
            username='user1',
            password='password123'
        )

        with self.assertRaises(Exception):

            User.objects.create_user(
                email='test@example.com',
                username='user2',
                password='password123'
            )
            

class UserAPITests(APITestCase):

    def test_register_user(self):

        payload = {
            'email': 'test@example.com',
            'username': 'testuser',
            'password': 'password123'
        }

        response = self.client.post(
            '/api/users/register/',
            payload
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            User.objects.count(),
            1
        )

    def test_login_user_jwt(self):

        User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='password123'
        )

        payload = {
            'email': 'test@example.com',
            'password': 'password123'
        }

        response = self.client.post(
            '/api/token/',
            payload
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertIn('access', response.data)

    def test_unauthorized_access(self):

        response = self.client.get(
            '/api/users/me/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )