from django.urls import path
from .views import chart_focus_list, chart_focus_detail, chart_interviewed_list, chart_interviewed_detail, chart_requirement_list, chart_requirement_detail, chart_type_list, chart_type_detail, employee_list, employee_detail, user_department_list, user_department_detail, user_role_list, user_role_detail

urlpatterns = [
     path('user_role/', user_role_list, name='user_role_list'),
    path('user_role/<int:pk>/', user_role_detail, name='user_role_detail'),
    path('user_department/', user_department_list, name='user_department_list'),
    path('user_department/<int:pk>/', user_department_detail, name='user_department_detail'),
    path('employee/', employee_list, name='employee-list'),
    path('employee/<int:pk>/', employee_detail, name='employee-detail'),
    path('chart_type/', chart_type_list, name='chart_type_list'),
    path('chart_type/<int:pk>/', chart_type_detail, name='chart_type_detail'),
    path('chart_requirement/', chart_requirement_list, name='chart_requirement_list'),
    path('chart_requirement/<int:pk>/', chart_requirement_detail, name='chart_requirement_detail'),
    path('chart_intervieweds/', chart_interviewed_list, name='chart_interviewed_list'),
    path('chart_intervieweds/<int:pk>/', chart_interviewed_detail, name='chart_interviewed_detail'),
    path('chart_focus/', chart_focus_list, name='chart_focus_list'),
    path('chart_focus/<int:pk>/', chart_focus_detail, name='chart_focus_detail'),

]