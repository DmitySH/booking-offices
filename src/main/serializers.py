from rest_framework import serializers

from src.main import models


class OfficeSerializer(serializers.ModelSerializer):
    """
    Serializes office.
    """

    class Meta:
        model = models.Office
        fields = '__all__'
