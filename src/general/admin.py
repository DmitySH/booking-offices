from django.contrib import admin

from src.general.models import Country, City, RatingStar


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    pass
