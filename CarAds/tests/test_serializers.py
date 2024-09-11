from CarAds.serializers import CarAdsSerializer, UserSerializer
import pytest


@pytest.mark.django_db
def test_car_ads_serializer(car_ads_factory):
    car = car_ads_factory()
    serializer = CarAdsSerializer(car)
    assert serializer.data['code'] == car.code


@pytest.mark.django_db
def test_user_serializer(user_factory):
    user = user_factory(email='test@example.com')
    serializer = UserSerializer(user)
    assert serializer.data['email'] == user.email
