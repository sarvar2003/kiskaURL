from django.shortcuts import redirect
from rest_framework import generics, permissions
from rest_framework.views import APIView

from . import serializers
from . import models

class OriginalURLApiView(generics.ListCreateAPIView):
    """API view for listing and creating OriginalURL"""

    serializer_class = serializers.OriginalUrlSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.OriginalURL.objects.all()


class RedirectURLApiView(APIView):
    """API view for redirecting short URLs"""

    def get(self, request, *args, **kwargs):
        url_object = models.OriginalURL.objects.get(url_hash=kwargs.get('pk'))
        url_object.visited += 1
        url_object.save()
        return redirect(url_object.url)