from django.db.models import Model, IntegerField, OneToOneField, ForeignKey
from django.db.models import CASCADE, RESTRICT

from django.contrib.auth.models import User

from user_departments.models import UserDepartment
from user_roles.models import UserRole

# Create your models here.


class Employee(Model):
    id = IntegerField("id", primary_key=True)
    role_id = ForeignKey(UserRole, on_delete=RESTRICT)
    department_id = ForeignKey(UserDepartment, on_delete=RESTRICT)
    user = OneToOneField(User, on_delete=CASCADE)  # maybe change next feature

    class Meta:
        db_table = "employee"
        ordering = ["id"]
