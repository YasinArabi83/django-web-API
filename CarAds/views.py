from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action

from .serializers import CarAdsSerializer, UserSerializer

from .pagination import CustomPagination
from .models import CarAds


class CarAdsViewSet(viewsets.ModelViewSet):
    queryset = CarAds.objects.all()
    serializer_class = CarAdsSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'], url_path='type/(?P<body_type>[^/.]+)')
    def filter_by_type(self, request, body_type=None):
        body_type = body_type.lower()
        all_body_types = ("crossover", "suv", "hatchback", "passenger_car")
        if body_type not in all_body_types:
            return Response({"detail": "Car type not found."}, status=status.HTTP_404_NOT_FOUND)

        cars = CarAds.objects.filter(body_type=body_type)

        page = self.paginate_queryset(cars)
        if page is not None:
            serializer = CarAdsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = CarAdsSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


User = get_user_model()


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
