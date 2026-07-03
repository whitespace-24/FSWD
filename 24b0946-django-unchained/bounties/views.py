from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Bounty
from .serializers import UserSerializer, BountySerializer

# POST /api/auth/register/
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

# GET and POST /api/bounties/
class BountyListCreate(generics.ListCreateAPIView):
    serializer_class = BountySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bounty.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# GET, PUT, PATCH, DELETE /api/bounties/<id>/
class BountyDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BountySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Bounty.objects.filter(owner=self.request.user)