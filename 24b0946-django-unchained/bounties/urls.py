from django.urls import path
from .views import RegisterView, BountyListCreate, BountyDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # Auth endpoints
    path('auth/register/', RegisterView.as_view()),
    path('auth/login/', TokenObtainPairView.as_view()),
    path('auth/refresh/', TokenRefreshView.as_view()),
    
    # Bounty endpoints
    path('bounties/', BountyListCreate.as_view()),
    path('bounties/<int:pk>/', BountyDetail.as_view()),
]