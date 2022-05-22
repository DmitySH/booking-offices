from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение',
                                             validators=[MinValueValidator(1),
                                                         MaxValueValidator(5)],
                                             unique=True)

    def __str__(self):
        return 'Оценка {}'.format(self.value)

    class Meta:
        ordering = ['value']
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
