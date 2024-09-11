from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarAdsViewSet, ChangePasswordView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView
router = DefaultRouter()
router.register(r'car', CarAdsViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
