from django import views
from django.urls import path

from .routes import getRoutes
from .views import *



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', getRoutes.as_view()),
    path('company/', company.as_view()),
    path('company/<str:uuid>/', companyDetail.as_view()),
    path('company/<str:uuid>/team/', team.as_view()),
    path('search/', search.as_view()),
    path('team/', getTeam.as_view()),

    # Your other URL entries.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


