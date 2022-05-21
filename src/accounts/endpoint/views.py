from rest_framework import viewsets, permissions

from .. import serializers


class UserView(viewsets.ModelViewSet):
    """
    Gets and edits user data.
    """

    serializer_class = serializers.ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user

    def get_object(self):
        return self.get_queryset()
