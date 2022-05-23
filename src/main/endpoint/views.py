from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser

from src.main import serializers
from src.main.models import Office, OfficePhoto
from src.main.permissions import IsModeratorOrReadOnly


class OfficePhotoView(viewsets.ModelViewSet):
    serializer_class = serializers.OfficePhotoSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsModeratorOrReadOnly]

    def get_queryset(self):
        office_id = self.kwargs['office_id']
        return OfficePhoto.objects.filter(office=office_id)


class OfficeView(viewsets.ModelViewSet):
    """
    Gets and edits office data.
    """

    serializer_class = serializers.OfficeSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def get_queryset(self):
        return Office.objects.all()
