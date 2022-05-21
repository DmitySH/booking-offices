from rest_framework import serializers

from . import models


class TokenAuthenticateSerializer(serializers.Serializer):
    """
    Serializes data for user's authentication.
    """

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}
    )


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes authorized user's profile.
    """

    email = serializers.EmailField(read_only=True)
    join_date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = models.Profile
        fields = (
            'email', 'first_name', 'last_name', 'country', 'city', 'biography',
            'join_date')
