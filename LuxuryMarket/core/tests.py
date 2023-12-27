# core/tests.py
from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user, bio='Test bio')

    def test_user_profile_view(self):
        response = self.client.get('/api/user/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test bio')

