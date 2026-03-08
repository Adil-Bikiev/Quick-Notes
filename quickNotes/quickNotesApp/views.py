from rest_framework import viewsets, permissions, filters
from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)