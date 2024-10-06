from django.urls import path
from . import views

urlpatterns = [
    path('sensor_chart/', views.sensor_chart_list, name='sensor_chart_list'),
    path('sensor_chart/<int:pk>/', views.sensor_chart_detail, name='sensor_chart_detail'),
    path('sensor_chart/project/<int:project_id>/', views.sensor_chart_list_by_project, name='sensor_chart_list_by_project')

    
]