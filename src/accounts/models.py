from django.db import models


class AuthUser(models.Model):
    """
    Extension of user model.
    """

    email = models.EmailField(max_length=100, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    biography = models.TextField(max_length=2000, blank=True, null=True)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
