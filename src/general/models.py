from django.db import models


class Country(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        models.Index(fields=['name'])
        ordering = ['name']
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class City(models.Model):
    name = models.CharField('Название', max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        models.Index(fields=['name'])
        ordering = ['name']
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
