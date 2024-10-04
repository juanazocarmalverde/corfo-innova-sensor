from django.urls import path
from .views import user_role_list, user_role_detail

urlpatterns = [
    path('user_role/', user_role_list, name='user_role_list'),
    path('user_role/<int:pk>/', user_role_detail, name='user_role_detail'),

]