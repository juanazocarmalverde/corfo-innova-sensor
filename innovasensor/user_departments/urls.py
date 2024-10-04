from django.urls import path
from .views import user_department_list, user_department_detail

urlpatterns = [
    path('user_department/', user_department_list, name='user_department_list'),
    path('user_department/<int:pk>/', user_department_detail, name='user_department_detail'),

]