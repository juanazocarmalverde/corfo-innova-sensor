from django.db.models import Model, IntegerField, CharField

# Create your models here.


class ChartInterviewed(Model):
    id = IntegerField("id", primary_key=True)
    text = CharField("text", max_length=256, blank=False, null=False)

    class Meta:
        db_table = "chart_interviewed"
        ordering = ["id"]
