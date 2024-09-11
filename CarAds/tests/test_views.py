from django.urls import reverse
import pytest


@pytest.mark.django_db
def test_car_ads_list_view_unauthenticated(api_client):

    response = api_client.get(reverse('carads-list'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_car_ads_create_view_unauthenticated(api_client, car_ads_data):

    response = api_client.post(reverse('carads-list'), car_ads_data)
    assert response.status_code == 401  # Unauthorized


@pytest.mark.django_db
def test_car_ads_create_view_authenticated(api_client, user_token, car_ads_data):

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access_token'])
    response = api_client.post(reverse('carads-list'), car_ads_data)
    assert response.status_code == 201  # Created


@pytest.mark.django_db
def test_car_ads_list_authenticated(api_client, user_token, car_ads_data, car_ads_factory):

    car_ads_factory(**car_ads_data)
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access_token'])
    response = api_client.get(reverse('carads-list'))
    assert response.status_code == 200
    assert len(response.data['results']) == 1


@pytest.mark.django_db
def test_change_password_unauthenticated(api_client):

    data = {
        'old_password': 'password123',
        'new_password': 'newpassword123'
    }
    response = api_client.post(reverse('change-password'), data)
    assert response.status_code == 401  # Unauthorized


@pytest.mark.django_db
def test_change_password_authenticated(api_client, user_token):

    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + user_token['access_token'])
    data = {
        'old_password': 'password123',
        'new_password': 'newpassword123'
    }
    response = api_client.post(reverse('change-password'), data)
    assert response.status_code == 200
    assert response.data['detail'] == 'Password updated successfully.'
