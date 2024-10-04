from django.db.models import Model, IntegerField, TextField
# Create your models here.

class ChartFocus(Model):
    id = IntegerField("id", primary_key=True)
    text = TextField("text", max_length=256, null=False)

    class Meta:
        db_table = "chart_focus"
        ordering = ["id"]
