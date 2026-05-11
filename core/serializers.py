from rest_framework import serializers

from . import models
from .services.url_services import create_or_get_short_url

class OriginalUrlSerializer(serializers.ModelSerializer):
    """Serializer for Original URL API View"""

    class Meta:
        model = models.OriginalURL
        fields = (
            'id',
            'user',
            'get_user_username',
            'url',
            'shortened',
            'visited',
            'date_created',
            'short_url',
            'url_hash',
        )

        read_only_fields = (
            'user',
            'url_hash',
            'short_url',
            'visited',
            'shortened',
        )

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user
        return attrs

    def create(self, validated_data):
        user = self.validated_data["user"]
        url_value = self.validated_data["url"]

        return create_or_get_short_url(user, url_value)
