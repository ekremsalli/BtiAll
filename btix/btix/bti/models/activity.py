from django.db import models


class TaskActivity(models.Model):
    name = models.CharField(max_length=65, db_index=True)
    is_success = models.BooleanField(db_index=True)
    params = models.TextField(null=True, blank=True)
    exception = models.TextField(null=True, blank=True)
    took = models.FloatField(default=0)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "btix_activity"
        ordering = ["-id"]
