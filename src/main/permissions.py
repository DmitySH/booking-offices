from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsModeratorOrReadOnly(BasePermission):
    """
    The request is authenticated as a user and is moderator,
    or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and request.user.groups.filter(
                name='Модераторы').exists()
        )
