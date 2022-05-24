from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

import src.general.models as general_models
from src.accounts.models import Profile


class Office(models.Model):
    title = models.CharField('Краткое описание', max_length=127, unique=True)
    country = models.ForeignKey(general_models.Country,
                                on_delete=models.CASCADE,
                                verbose_name='Страна',
                                related_name='offices')
    city = models.ForeignKey(general_models.City, on_delete=models.CASCADE,
                             verbose_name='Город',
                             related_name='offices')
    address = models.CharField('Адерес', max_length=255)
    description = models.TextField('Описание', max_length=2000)
    price_per_hour = models.PositiveIntegerField('Цена за час аренды')
    prepayment_percentage = models.PositiveIntegerField(
        'Процент залога для брони', validators=[MaxValueValidator(100)])

    def __str__(self):
        return 'Кабинет {}'.format(self.title)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'


class OfficePhoto(models.Model):
    text = models.CharField('Описание фотографии', max_length=255)
    photo = models.ImageField('Фотография', upload_to='office-photos/')
    office = models.ForeignKey(Office, on_delete=models.CASCADE,
                               verbose_name='Кабинет', related_name='photos')

    def __str__(self):
        return 'Фотография кабинета {}'.format(self.office.title)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Фотография кабинета'
        verbose_name_plural = 'Фотографии кабинетов'


class OfficeReview(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE,
                               verbose_name='Кабинет', related_name='reviews')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                verbose_name='Аккаунт',
                                related_name='sent_reviews')
    text = models.TextField('Текст отзыва', max_length=2000)
    rating = models.PositiveSmallIntegerField('Оценка',
                                              validators=[MinValueValidator(1),
                                                          MaxValueValidator(
                                                              5)])
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return 'Отзыв на кабинет {}'.format(self.office.title)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Reservation(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE,
                               verbose_name='Кабинет',
                               related_name='reservations')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,
                                verbose_name='Аккаунт',
                                related_name='reservations')
    start = models.DateTimeField('Начало аренды')
    end = models.DateTimeField('Конец аренды')

    def __str__(self):
        return 'Бронь кабинета {}'.format(self.office.title)

    class Meta:
        ordering = ['start']
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
