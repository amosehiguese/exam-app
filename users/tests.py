from django.utils import timezone
from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        now = timezone.now()
        user = User.objects.create_user(
            email='testuser@email.com',
            password='testing123',

        )
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertTrue(user.check_password('testing123'))
        self.assertFalse(user.check_password('wrongpassword'))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified)
        self.assertTrue(user.date_joined)
