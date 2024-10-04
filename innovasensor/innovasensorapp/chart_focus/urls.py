from django.urls import path
from . import views

urlpatterns = [
    path('chart_focus/', views.chart_focus_list, name='chart_focus_list'),
    path('chart_focus/<int:pk>/', views.chart_focus_detail, name='chart_focus_detail'),

]