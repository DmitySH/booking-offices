from django.contrib.auth.models import User, AbstractUser
from django.db import models

from src.accounts.managers import ProfileManager


class Profile(AbstractUser):
    """
    New user model.
    """

    objects = ProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    date_joined = None
    username = None

    email = models.EmailField(verbose_name='Электронный адрес', unique=True)

    first_name = models.CharField(verbose_name='Имя', max_length=30,
                                  blank=True, default='')
    last_name = models.CharField(verbose_name='Фамилия', max_length=30,
                                 blank=True, default='')

    join_date = models.DateTimeField(verbose_name='Дата регистрации',
                                     auto_now_add=True)
    country = models.CharField(verbose_name='Страна', max_length=30,
                               blank=True, default='')
    city = models.CharField(verbose_name='Город', max_length=30,
                            blank=True, default='')
    biography = models.TextField(verbose_name='Биография',
                                 max_length=2000, blank=True, default='')

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
