from rest_framework import viewsets, permissions

from .models import Note
from .models import Body
from .models import Chisme
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = NoteSerializer
class BodyViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = NoteSerializer
class ChismeViewSet(viewsets.ModelViewSet):
    queryset = Body.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = NoteSerializer