from django.urls import path
from . import views

urlpatterns = [
    path('user_department/', views.user_department_list, name='user_department_list'),
    path('user_department/<int:pk>/', views.user_department_detail, name='user_department_detail'),

]