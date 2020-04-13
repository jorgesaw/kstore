"""TestProfile test."""

# Django
from django.test import TestCase

# Models
from apps.registration.models import Profile
from django.contrib.auth.models import User


class ProfileTestCase(TestCase):
    """Profile test case."""

    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)