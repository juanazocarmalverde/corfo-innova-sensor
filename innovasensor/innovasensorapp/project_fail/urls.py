from django.urls import path
from . import views

urlpatterns = [
    path('project_fail/', views.project_fail_list, name='project_fail_list'),
    path('project_fail/<int:pk>/', views.project_fail_detail, name='project_fail_detail'),
    
]