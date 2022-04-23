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

    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}
    )


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializes authorized user's profile.
    """

    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)

    class Meta:
        model = models.Profile
        fields = ('username', 'email', 'country', 'city', 'biography',)
