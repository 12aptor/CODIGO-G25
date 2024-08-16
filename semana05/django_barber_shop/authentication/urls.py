from django.urls import path
from rest_framework_simplejwt.views import (
    # TokenObtainPairView,
    TokenRefreshView
)
from .views import *

urlpatterns = [
    path('role/list/', RoleListView.as_view()),
    path('role/create/', RoleCreateView.as_view()),
    path('role/update/<int:pk>/', RoleUpdateView.as_view()),
    path('role/delete/<int:pk>/', RoleDestroyView.as_view()),

    path('user/list/', UserListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/update/<int:pk>/', UserUpdateView.as_view()),
    path('user/delete/<int:pk>/', UserDestroyView.as_view()),

    # path('login/', TokenObtainPairView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]