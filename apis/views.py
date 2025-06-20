from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@extend_schema(
    request=UserSerializer,
    responses={201: None},
    description="Register a new user with email and password.",
    tags=["Auth"]
)
class UserListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

