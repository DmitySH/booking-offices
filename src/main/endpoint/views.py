from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from src.main import serializers
from src.main.exceptions import IncorrectMethod
from src.main.models import Office, OfficePhoto, OfficeReview
from src.main.permissions import IsModeratorOrReadOnly


class OfficeReviewView(viewsets.ModelViewSet):
    serializer_class = serializers.OfficeReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        review_id = self.kwargs['review_id']
        return get_object_or_404(OfficeReview, id=review_id)

    def get_queryset(self):
        office_id = self.kwargs['office_id']
        return OfficeReview.objects.filter(office=office_id)

    def perform_create(self, serializer):
        if OfficeReview.objects.filter(profile=self.request.user,
                                       office=serializer.validated_data[
                                           'office']).exists():
            raise IncorrectMethod(
                detail='Use PUT method to edit existing review')
        serializer.save(profile=self.request.user)

    def perform_update(self, serializer):
        # Ignore office to update, because it was defined in URL.
        serializer.validated_data.pop('office')
        serializer.save()


class OfficePhotoView(viewsets.ModelViewSet):
    serializer_class = serializers.OfficePhotoSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsModeratorOrReadOnly]

    def get_object(self):
        photo_id = self.kwargs['photo_id']
        return get_object_or_404(OfficePhoto, id=photo_id)

    def get_queryset(self):
        office_id = self.kwargs['office_id']
        return OfficePhoto.objects.filter(office=office_id)

    def perform_destroy(self, instance):
        if instance.photo:
            instance.photo.delete()
        return super().perform_destroy(instance)


class OfficeView(viewsets.ModelViewSet):
    """
    Gets and edits office data.
    """

    serializer_class = serializers.OfficeSerializer
    permission_classes = [IsModeratorOrReadOnly]

    def get_queryset(self):
        return Office.objects.all()
