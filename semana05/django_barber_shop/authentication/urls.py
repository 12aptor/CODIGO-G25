from django.urls import path
from .views import *

urlpatterns = [
    path('role/list/', RoleListView.as_view()),
    path('role/create/', RoleCreateView.as_view())
]