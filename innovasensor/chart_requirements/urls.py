from django.urls import path
from .views import chart_requirement_list, chart_requirement_detail

urlpatterns = [
    path('chart_requirement/', chart_requirement_list, name='chart_requirement_list'),
    path('chart_requirement/<int:pk>/', chart_requirement_detail, name='chart_requirement_detail'),

]