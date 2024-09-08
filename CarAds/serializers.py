from rest_framework import serializers

from CarAds.models import CarAds
from django.contrib.auth import get_user_model


class CarAdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarAds
        fields = '__all__'


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'password_confirm')

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirm')  # Remove the password_confirm field
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)  # Set the user's password
        user.save()
        return user