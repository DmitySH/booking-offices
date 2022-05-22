from rest_framework import viewsets

from src.main import serializers
from src.main.models import Office
from src.main.permissions import IsModeratorOrReadOnly


class OfficeView(viewsets.ModelViewSet):
    """
    Gets and edits office data.
    """

    serializer_class = serializers.OfficeSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def get_queryset(self):
        return Office.objects.all()
