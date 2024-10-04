from django.contrib import admin
from .models import ChartFocus
from .models import ChartInterviewed
from .models import ChartRequirement
from .models import ChartType
from .models import Employee
from .models import UserDepartment
from .models import UserRole

admin.site.register(UserRole)
admin.site.register(UserDepartment)
admin.site.register(Employee)
admin.site.register(ChartType)
admin.site.register(ChartRequirement)
admin.site.register(ChartInterviewed)
admin.site.register(ChartFocus)