from django.db.models import Model, IntegerField, TextField, OneToOneField, ForeignKey, CharField
from django.db.models import CASCADE, RESTRICT
from django.contrib.auth.models import User


class UserDepartment(Model):
    id = IntegerField("id", primary_key=True)
    name = CharField("name", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "user_department"
        ordering = ["id"]


class UserRole(Model):
    id = IntegerField("id", primary_key=True)
    name = CharField("name", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "user_role"
        ordering = ["id"]

# Create your models here.
class Employee(Model):
    id = IntegerField("id", primary_key=True)
    role_id = ForeignKey(UserRole, on_delete=RESTRICT)
    department_id = ForeignKey(UserDepartment, on_delete=RESTRICT)
    user = OneToOneField(User, on_delete=CASCADE)  # maybe change next feature

    class Meta:
        db_table = "employee"
        ordering = ["id"]


class ChartFocus(Model):
    id = IntegerField("id", primary_key=True)
    text = TextField("text", max_length=256, null=False)

    class Meta:
        db_table = "chart_focus"
        ordering = ["id"]

class ChartInterviewed(Model):
    id = IntegerField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_interviewed"
        ordering = ["id"]

class ChartRequirement(Model):
    id = IntegerField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_requirement"
        ordering = ["id"]


class ChartType(Model):
    id = IntegerField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_types"
        ordering = ["id"]