from django.db.models import Model, IntegerField, CharField

# Create your models here.

class UserDepartment(Model):
    id = IntegerField("id", primary_key=True)
    name = CharField("name", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "user_department"
        ordering = ["id"]