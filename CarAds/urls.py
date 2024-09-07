from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarAdsViewSet

router = DefaultRouter()
router.register(r'car', CarAdsViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
