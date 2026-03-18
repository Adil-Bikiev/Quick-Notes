from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "title", "content", "color", "reminder_at", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")