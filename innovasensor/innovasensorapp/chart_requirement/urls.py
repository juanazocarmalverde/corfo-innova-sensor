from django.urls import path
from . import views

urlpatterns = [
    path('chart_requirement/', views.chart_requirement_list, name='chart_requirement_list'),
    path('chart_requirement/<int:pk>/', views.chart_requirement_detail, name='chart_requirement_detail'),

]