from django.urls import path
from . import views

urlpatterns = [
    path('project_fails/', views.project_fail_list, name='project_fail_list'),
    path('project_fails/<int:pk>/', views.project_fail_detail, name='project_fail_detail'),
    
]