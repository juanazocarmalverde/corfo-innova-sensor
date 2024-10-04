from django.urls import path
from . import views

urlpatterns = [
    path('sensor_charts/', views.sensor_charts_list, name='sensor_charts_list'),
    path('sensor_charts/<int:pk>/', views.sensor_charts_detail, name='sensor_charts_detail'),
    
]