from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Extension of user model.
    """

    User._meta.get_field('email')._unique = True
    User._meta.get_field('email').blank = False
    User._meta.get_field('email').null = False

    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name="profile")
    join_date = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    biography = models.TextField(max_length=2000, blank=True, null=True)

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
