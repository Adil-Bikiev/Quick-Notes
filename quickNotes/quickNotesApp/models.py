from django.db import models

class Note(models.Model):
    COLOR_CHOICES = [
        ('white', '⚪ Default'),
        ('red', '🔴 Urgent'),
        ('yellow', '🟡 Important'),
        ('green', '🟢 Done'),
        ('blue', '🔵 Idea'),
        ('purple', '🟣 Personal'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, default='white')
    reminder_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return self.title