from django.db import models
from django.contrib.auth import get_user_model


class ShortURL(models.Model):
    """Database model for URLs"""
    
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    url = models.URLField(max_length=2048)
    shortened = models.IntegerField(default=1, editable=False)
    url_hash = models.CharField(max_length=200, default="")
    short_url = models.URLField(max_length=2048, default="")
    date_created = models.DateTimeField(auto_now_add=True)
    visited = models.IntegerField(default=0)


    @property
    def get_user_username(self):
        return self.user.username
    
    def __str__(self) -> str:
        return f"\nURL: {self.url}\nUSER: {self.user.user_name}\nDATE_CREATED: {self.date_created}\n\n"
