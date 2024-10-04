"""
URL configuration for innovasensor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),  # Endpoints para login, logout y password reset
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),  # Endpoints para registro de usuario
    path('api/', include('innovasensorapp.chart_focus.urls')),
    path('api/', include('innovasensorapp.chart_interviewds.urls')),
    path('api/', include('innovasensorapp.chart_requirement.urls')),
    path('api/', include('innovasensorapp.chart_type.urls')),
    path('api/', include('innovasensorapp.employee.urls')),
    path('api/', include('innovasensorapp.user_department.urls')),
    path('api/', include('innovasensorapp.user_role.urls')),
    
]
