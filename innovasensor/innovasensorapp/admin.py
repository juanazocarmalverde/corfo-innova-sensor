from django.contrib import admin
from .models import ChartFocus, ChartInterviewed, ChartRequirement, ChartType, Employee, UserDepartment, UserRole, ProjectFail, Project, SensorChart

admin.site.register(UserRole)
admin.site.register(UserDepartment)
admin.site.register(Employee)
admin.site.register(ChartType)
admin.site.register(ChartRequirement)
admin.site.register(ChartInterviewed)
admin.site.register(ChartFocus)
admin.site.register(ProjectFail)
admin.site.register(Project)
admin.site.register(SensorChart)