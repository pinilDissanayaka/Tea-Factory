from django.db import models
from django.contrib.auth.models import User

class TeaLeaves(models.Model):
    quality=models.CharField(max_length=100)
    quantity=models.FloatField(max_length=100)
    description=models.TextField(max_length=100, blank=True, null=True)
    collector_at=models.DateTimeField(auto_now_add=True)
    collector_name=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="collector_name")
