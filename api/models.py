from django.db import models


class TeaLeaves(models.Model):
    provider_name = models.CharField(max_length=120)
    collected_weight=models.FloatField()
    any_note=models.TextField(null=True, blank=True)
    collected_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f"{self.provider_name} gives {self.collected_weight} at {self.collected_date}")
    
    