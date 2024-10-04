from django.urls import path
from .views import chart_interviewed_list, chart_interviewed_detail

urlpatterns = [
    path('chart_intervieweds/', chart_interviewed_list, name='chart_interviewed_list'),
    path('chart_intervieweds/<int:pk>/', chart_interviewed_detail, name='chart_interviewed_detail'),

]