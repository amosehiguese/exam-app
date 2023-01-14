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

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            email='superuser@email.com',
            password='superuser123',
        )

        self.assertEqual(user.email, 'superuser@email.com')
        self.assertTrue(user.check_password('superuser123'))
        self.assertFalse(user.check_password('wrongpass'))
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_verified)
        self.assertTrue(user.date_joined)