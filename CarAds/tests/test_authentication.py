from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_signup_view(api_client):
    data = {
        'email': 'newuser@example.com',
        'password': 'password123',
        'password_confirm': 'password123'
    }
    response = api_client.post(reverse('signup'), data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_login_view(api_client, user_factory):
    user = user_factory(email='test@example.com', password='testpass123')
    data = {
        'email': user.email,
        'password': 'testpass123'
    }
    response = api_client.post(reverse('login'), data)
    assert response.status_code == 200
