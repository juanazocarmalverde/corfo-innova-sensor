from django.urls import path
from . import views

urlpatterns = [
    path('chart_intervieweds/', views.chart_interviewed_list, name='chart_interviewed_list'),
    path('chart_intervieweds/<int:pk>/', views.chart_interviewed_detail, name='chart_interviewed_detail'),

]