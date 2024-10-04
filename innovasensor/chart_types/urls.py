from django.urls import path
from .views import chart_type_list, chart_type_detail

urlpatterns = [
    path('chart_type/', chart_type_list, name='chart_type_list'),
    path('chart_type/<int:pk>/', chart_type_detail, name='chart_type_detail'),

]