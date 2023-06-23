from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Create your tests here.

class SignupAPITests(TestCase):

    def test_signup_with_valid_data(self):
        client = APIClient()
        data = {
            "username": "test_user",
            "email": "test_user@example.com",
            "password": "password123",
        }
        response = client.post("/api/signup", data=data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.data["username"] == "test_user")

    def test_signup_with_invalid_data(self):
        client = APIClient()
        data = {
            "username": "",
            "email": "test_user@example.com",
            "password": "password123",
        }
        response = client.post("/api/signup", data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["username"], ["This field is required."])


class LoginAPITests(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            username="test_user", email="test_user@example.com", password="password123"
        )

    def test_login_with_valid_credentials(self):
        client = APIClient()
        data = {
            "username": "test_user",
            "password": "password123",
        }
        response = client.post("/api/login", data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["token"])

    def test_login_with_invalid_credentials(self):
        client = APIClient()
        data = {
            "username": "test_user",
            "password": "wrong_password",
        }
        response = client.post("/api/login", data=data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data["detail"], "Incorrect username or password.")
