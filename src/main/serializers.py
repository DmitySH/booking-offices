from rest_framework import serializers

from src.general.models import Country, City
from src.main import models


class OfficePhotoSerializer(serializers.ModelSerializer):
    """
    Serializes photo of office.
    """

    class Meta:
        model = models.OfficePhoto
        fields = '__all__'


class OfficeSerializer(serializers.ModelSerializer):
    """
    Serializes office.
    """

    country = serializers.CharField(source='country.name')
    city = serializers.CharField(source='city.name')

    class Meta:
        model = models.Office
        fields = '__all__'

    def validate(self, attrs):
        errors = dict()
        try:
            attrs['country'] = Country.objects.get(**attrs['country'])
        except Country.DoesNotExist:
            errors['country'] = 'No such country'

        try:
            attrs['city'] = City.objects.get(**attrs['city'])
        except City.DoesNotExist:
            errors['city'] = 'No such city'

        if len(errors) > 0:
            raise serializers.ValidationError(errors)

        return super().validate(attrs)

    def update(self, instance, validated_data):
        instance.country = validated_data.pop('country')
        instance.city = validated_data.pop('city')

        return super().update(instance, validated_data)
