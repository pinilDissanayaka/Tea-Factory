from django.db import models
from uuid import uuid4


class TeaLeaves(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    provider_name = models.CharField(max_length=120)
    collected_weight = models.DecimalField(max_digits=100, decimal_places=3)
    any_note = models.TextField(null=True, blank=True)
    collected_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider_name} gives {self.collected_weight} at {self.collected_date}"
    
    