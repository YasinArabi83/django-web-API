from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CarAdsSerializer, UserSerializer

from .pagination import CustomPagination
from .models import CarAds


class CarAdsViewSet(viewsets.ModelViewSet):
    queryset = CarAds.objects.all()
    serializer_class = CarAdsSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
