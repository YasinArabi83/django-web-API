from rest_framework import viewsets
from .models import CarAds
from .serializers import CarAdsSerializer


class CarAdsViewSet(viewsets.ModelViewSet):
    queryset = CarAds.objects.all()
    serializer_class = CarAdsSerializer
