from django.urls import path
from .views import *

urlpatterns = [
    path('role/list/', RoleListView.as_view()),
    path('role/create/', RoleCreateView.as_view()),
    path('role/update/<int:pk>/', RoleUpdateView.as_view()),
    path('role/delete/<int:pk>/', RoleDestroyView.as_view()),

    path('user/list/', UserListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
]