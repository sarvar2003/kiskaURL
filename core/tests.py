from rest_framework.test import APITestCase
from rest_framework import status

from django.contrib.auth import get_user_model


User = get_user_model()


class URLAPITests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            email='test@example.com',
            username='testuser',
            password='password123'
        )

        response = self.client.post(
            '/api/token/',
            {
                'email': 'test@example.com',
                'password': 'password123'
            }
        )

        self.token = response.data['access']

    def test_create_short_url(self):

        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token}'
        )

        payload = {
            'url': 'https://google.com'
        }

        response = self.client.post(
            '/api/urls/',
            payload
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertIn(
            'short_url',
            response.data
        )

    def test_unauthenticated_user_cannot_create_url(self):

        response = self.client.post(
            '/api/urls/',
            {
                'url': 'https://google.com'
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )   