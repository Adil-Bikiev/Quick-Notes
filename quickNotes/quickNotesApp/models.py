from django.conf import settings
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notes")

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title