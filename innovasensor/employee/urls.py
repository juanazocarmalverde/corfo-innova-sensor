from django.urls import path
from .views import employee_list, employee_detail

urlpatterns = [
    path('employee/', employee_list, name='employee-list'),
    path('employee/<int:pk>/', employee_detail, name='employee-detail'),

]