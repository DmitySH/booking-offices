from django.contrib.auth.models import User, AbstractUser
from django.db import models

import src.general.models as general_models
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
    country = models.ForeignKey(general_models.Country,
                                on_delete=models.CASCADE,
                                verbose_name='Страна',
                                related_name='profiles',
                                null=True)
    city = models.ForeignKey(general_models.City,
                             on_delete=models.CASCADE,
                             verbose_name='Город',
                             related_name='profiles',
                             null=True)
    biography = models.TextField(verbose_name='Биография',
                                 max_length=2000, blank=True, default='')
    photo = models.ImageField('Фотография',
                              upload_to='profile-office-photos/',
                              null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-id']
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
