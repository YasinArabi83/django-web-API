from rest_framework import serializers

from CarAds.models import CarAds


class CarAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAds
        fields = '__all__'
