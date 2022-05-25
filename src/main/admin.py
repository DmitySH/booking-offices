from django.contrib import admin

from src.main.models import Office, Reservation, OfficeReview, OfficePhoto


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(OfficeReview)
class OfficeReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(OfficePhoto)
class OfficePhotoAdmin(admin.ModelAdmin):
    pass
