from django.db.models import Model, IntegerField, TextField, OneToOneField, ForeignKey, CharField, DateField, BooleanField, EmailField
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


class ProjectFail(Model):
    id = IntegerField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "project_fail"
        ordering = ["id"]


class Project(Model):
    id = IntegerField("id", primary_key=True)
    code = CharField("code", max_length=256, blank=False)
    justification = TextField("justification", max_length=256, null=True)
    women = BooleanField("women", default=True)
    sustainable = BooleanField("sustainable", default=True)
    url = CharField("url", max_length=256, blank=True)
    success = BooleanField("success", default=False)
    success_date = DateField("success date", null=True)
    description = TextField("description", max_length=256, blank=True)
    fail_id = ForeignKey(ProjectFail, on_delete=CASCADE)  # change next feature

    class Meta:
        db_table = "project"
        ordering = ["id"]


class SensorChart(Model):
    id = IntegerField("id", primary_key=True)
    executive = BooleanField("executive", default=True)
    email = EmailField("email")
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
    requirement_id = ForeignKey(ChartRequirement, CASCADE)  # change next feature
    type_id = ForeignKey(ChartType, CASCADE)  # change next feature
    focus_id = ForeignKey(ChartFocus, CASCADE)  # change next feature
    interviewed_id = ForeignKey(ChartInterviewed, CASCADE)  # change next feature
    user_id = ForeignKey(Employee, CASCADE)  # change next feature
    project_id = ForeignKey(Project, CASCADE)  # change next feature

    class Meta:
        db_table = "sensor_chart"
        ordering = ["id"]
