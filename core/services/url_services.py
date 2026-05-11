from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from ..models import urls
from ..utils.urls import utils


def create_or_get_short_url(user, original_url):
    
    """Handles URL creation and hashing logic"""

    instance = urls.ShortURL.objects.filter(
        user=user,
        url=original_url
        ).first()

    # URL already exists
    if instance:
        instance.shortened += 1
        instance.save(update_fields=["shortened"])
        return instance
    
    # URL does not exist
    instance = urls.ShortURL.objects.create(
        user=user,
        url=original_url
    )

    hashed_url = utils.hash_the_url(user, original_url)
    instance.hashed_url = hashed_url
    instance.short_url = f"{settings.DEFAULT_DOMAIN}{hashed_url}/"

    instance.save(update_fields=["url_hash", "short_url"])

    return instance
