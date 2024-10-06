from django.db.models import Model, IntegerField, TextField, OneToOneField, ForeignKey, CharField, DateField, BooleanField, EmailField
from django.db.models import CASCADE, RESTRICT
from django.contrib.auth.models import User
from django.db import models


class UserDepartment(Model):
    id = models.AutoField("id", primary_key=True)
    name = CharField("name", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "user_department"
        ordering = ["id"]


class UserRole(Model):
    id = models.AutoField("id", primary_key=True)
    name = CharField("name", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "user_role"
        ordering = ["id"]

# Create your models here.
class Employee(Model):
    id = models.AutoField("id", primary_key=True)
    role = ForeignKey(UserRole, on_delete=RESTRICT)
    department = ForeignKey(UserDepartment, on_delete=RESTRICT)
    user = OneToOneField(User, on_delete=CASCADE)  # maybe change next feature

    class Meta:
        db_table = "employee"
        ordering = ["id"]


class ChartFocus(Model):
    id = models.AutoField("id", primary_key=True)
    text = TextField("text", max_length=256, null=False)

    class Meta:
        db_table = "chart_focus"
        ordering = ["id"]

class ChartInterviewed(Model):
    id = models.AutoField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_interviewed"
        ordering = ["id"]

class ChartRequirement(Model):
    id = models.AutoField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_requirement"
        ordering = ["id"]


class ChartType(Model):
    id = models.AutoField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_types"
        ordering = ["id"]


class ProjectFail(Model):
    id = models.AutoField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "project_fail"
        ordering = ["id"]


class Project(Model):
    id = models.AutoField("id", primary_key=True)
    code = CharField("code", max_length=256, blank=False)
    justification = TextField("justification", max_length=256, null=True, blank=True)
    women = BooleanField("women", null=True, blank=True)
    sustainable = BooleanField("sustainable", null=True, blank=True)
    url = CharField("url", max_length=256, null=True, blank=True)
    success = BooleanField("success", null=True, blank=True)
    success_date = DateField("success date", null=True, blank=True)
    description = TextField("description", max_length=256, null=True, blank=True)
    fail = ForeignKey(ProjectFail, on_delete=CASCADE, null=True, blank=True)  # change next feature

    class Meta:
        db_table = "project"
        ordering = ["id"]


class SensorChart(Model):
    id = models.AutoField("id", primary_key=True)
    executive = BooleanField("executive", default=True)
    email = models.EmailField()
    sensor_chart_date = DateField("sensor chart date")
    first_evidence = TextField(
        "first evidence", max_length=256, null=False, blank=False
    )
    second_evidence = TextField(
        "second evidence", max_length=256, null=False, blank=False
    )
    third_evidence = TextField(
        "third evidence", max_length=256, null=False, blank=False
    )
    comment = TextField("comment", max_length=255, null=True, blank=True)
    requirement = models.ForeignKey(ChartRequirement, CASCADE, null=True, blank=True)  # change next feature
    chart_type = models.ForeignKey(ChartType, CASCADE, null=True, blank=True)  # change next feature
    focus = models.ForeignKey(ChartFocus, CASCADE, null=True, blank=True)  # change next feature
    interviewed = models.ForeignKey(ChartInterviewed, CASCADE, null=True, blank=True)  # change next feature
    employee = models.ForeignKey(Employee, CASCADE)  # change next feature
    project = models.ForeignKey(Project, CASCADE)  # change next feature

    class Meta:
        db_table = "sensor_chart"
        ordering = ["id"]
