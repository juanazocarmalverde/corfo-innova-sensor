from django.urls import path
from . import views

urlpatterns = [
    path('chart_type/', views.chart_type_list, name='chart_type_list'),
    path('chart_type/<int:pk>/', views.chart_type_detail, name='chart_type_detail'),

]