import pytest
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from CarAds.models import User, CarAds
from rest_framework.test import APIClient


@pytest.fixture
def car_ads_factory():
    def make_car_ad(**kwargs):
        defaults = {
            'code': '1234',
            'title': 'Test Car',
            'year': 2023,
            'mileage': 10000,
            'location': 'Tehran',
            'body_color': 'Red',
            'body_type': 'Sedan',
            'transmission': 'Automatic',
            'price': 50000000,
        }
        defaults.update(kwargs)
        return CarAds.objects.create(**defaults)

    return make_car_ad


@pytest.fixture
def user_factory(db):
    def create_user(**kwargs):
        password = kwargs.pop('password', 'password123')
        user = User.objects.create(**kwargs)
        user.set_password(password)
        user.save()
        return user

    return create_user


@pytest.fixture
def user_token(user_factory):
    user = user_factory(email='user@example.com', password='password123')
    access_token = AccessToken.for_user(user)
    refresh = RefreshToken.for_user(user)
    return {
        'access_token': str(access_token),
        'refresh_token': str(refresh)
    }


@pytest.fixture
def car_ads_data():
    return {
        'code': '5678',
        'title': 'New Car',
        'year': 2021,
        'mileage': 12000,
        'location': 'Tehran',
        'body_color': 'Blue',
        'body_type': 'Crossover',
        'transmission': 'Manual',
        'price': 10000000
    }


@pytest.fixture
def api_client():
    return APIClient()
