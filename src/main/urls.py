from django.urls import path

from src.main.endpoint import views

urlpatterns = [
    path('office/',
         views.OfficeView.as_view(
             {'get': 'list', 'post': 'create'})),
    path('office/<int:pk>/',
         views.OfficeView.as_view(
             {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('office/photo/',
         views.OfficePhotoView.as_view({'post': 'create'})),
    path('office/<int:office_id>/photos/',
         views.OfficePhotoView.as_view({'get': 'list'})),
    path('office/photos/<int:photo_id>/',
         views.OfficePhotoView.as_view({'delete': 'destroy'})),
    path('office/review/',
         views.OfficeReviewView.as_view({'post': 'create', 'put': 'update'})),
    path('office/<int:office_id>/reviews/',
         views.OfficeReviewView.as_view({'get': 'list'})),
    path('office/reviews/<int:review_id>/',
         views.OfficeReviewView.as_view({'delete': 'destroy'})),
    path('office/reservation/',
         views.ReservationView.as_view({'post': 'create'})),
    path('office/<int:office_id>/reservations/',
         views.ReservationView.as_view({'get': 'list'})),
    path('office/reservations/<int:reservation_id>/',
         views.ReservationView.as_view({'delete': 'destroy'})),
]
