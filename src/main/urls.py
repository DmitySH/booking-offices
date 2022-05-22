from django.urls import path

from src.main.endpoint import views

urlpatterns = [
    path('get-offices/', views.OfficeView.as_view({'get': 'list'})),
    path('get-offices/<int:pk>/',
         views.OfficeView.as_view({'get': 'retrieve'})),
]
