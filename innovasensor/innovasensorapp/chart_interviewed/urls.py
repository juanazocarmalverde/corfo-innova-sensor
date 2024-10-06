from django.urls import path
from . import views

urlpatterns = [
    path('chart_interviewed/', views.chart_interviewed_list, name='chart_interviewed_list'),
    path('chart_interviewed/<int:pk>/', views.chart_interviewed_detail, name='chart_interviewed_detail'),

]