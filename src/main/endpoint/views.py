from rest_framework import viewsets

from src.main import serializers
from src.main.models import Office


class OfficeView(viewsets.ModelViewSet):
    """
    Gets and edits office data.
    """

    serializer_class = serializers.OfficeSerializer

    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Office.objects.all()
