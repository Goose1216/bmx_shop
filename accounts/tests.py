from django.test import TestCase
from django.contrib.auth import get_user_model


from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserTest(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='test',
            email='test@mail.ru',
            password='testpass'
        )
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.email, 'test@mail.ru')
        self.assertEqual(user.password, 'testpass')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='supertest',
            email='supertest@mail.ru',
            password='supertestpass',
        )
        self.assertEqual(user.username, 'supertest')
        self.assertEqual(user.email, 'supertest@mail.ru')
        self.assertEqual(user.password, 'supertestpass')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_superuser)
