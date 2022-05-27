from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
path('projetos/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('projetos/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

path('', views.getRoutes),
path('projetos/', views.getProjects),
path('projetos/<str:pk>/', views.getProject),
]