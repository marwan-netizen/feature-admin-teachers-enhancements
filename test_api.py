import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lingopulse.settings')
django.setup()

from django.urls import reverse
from rest_framework.test import APIClient
from accounts.models import User

def test_auth_api():
    client = APIClient()
    # Check registration
    response = client.post('/core/api/v1/auth/register/', {
        'email': 'testuser@example.com',
        'password': 'testpassword123',
        'full_name': 'Test User',
        'role': 'student'
    })
    print(f"Register status: {response.status_code}")
    if response.status_code == 201:
        print("Registration successful")

    # Check me endpoint
    response = client.get('/core/api/v1/auth/me/')
    print(f"Me endpoint status: {response.status_code}")
    if response.status_code == 200:
        print(f"Me data: {response.data}")

if __name__ == "__main__":
    try:
        test_auth_api()
    except Exception as e:
        print(f"Error: {e}")
