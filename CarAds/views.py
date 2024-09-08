from rest_framework import viewsets
from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from .serializers import CarAdsSerializer, UserSerializer

from .models import CarAds


class CarAdsViewSet(viewsets.ModelViewSet):
    queryset = CarAds.objects.all()
    serializer_class = CarAdsSerializer


User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
