from django.urls import path
from djoser.views import UserViewSet

from .endpoint import views, auth_views

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('token/', auth_views.TokenAuthView.as_view()),
    path('register/', UserViewSet.as_view({'post': 'create'})),
]
