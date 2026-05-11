from django.contrib.auth import get_user_model
from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    """Serializer class for registering new users"""

    password = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
     )

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)
