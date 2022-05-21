from django.urls import path
from djoser.views import UserViewSet

from .endpoint import views, auth_views
from .endpoint.auth_views import ActivateUser

urlpatterns = [
    path('me/', views.UserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('token/', auth_views.TokenAuthView.as_view(), name='get-token'),
    path('register/', UserViewSet.as_view({'post': 'create'}),
         name='registration'),
    path('activate/<uid>/<token>',
         ActivateUser.as_view({'get': 'activation'}), name='activation'),
]
