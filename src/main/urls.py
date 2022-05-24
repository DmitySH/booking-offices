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
]
