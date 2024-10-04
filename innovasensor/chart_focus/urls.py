from django.urls import path
from .views import chart_focus_list, chart_focus_detail

urlpatterns = [
    path('chart_focus/', chart_focus_list, name='chart_focus_list'),
    path('chart_focus/<int:pk>/', chart_focus_detail, name='chart_focus_detail'),

]