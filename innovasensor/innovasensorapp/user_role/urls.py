from django.urls import path
from . import views

urlpatterns = [
    path('user_role/', views.user_role_list, name='user_role_list'),
    path('user_role/<int:pk>/', views.user_role_detail, name='user_role_detail'),
]