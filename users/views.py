from django.contrib.auth import get_user_model

from rest_framework import generics, permissions

from .serializers import UserSerializer


User = get_user_model()


class RegisterUserView(generics.CreateAPIView):
    """Register a new user"""

    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    """List all users (admin only)"""

    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class MeView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve/update/delete current authenticated user"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user