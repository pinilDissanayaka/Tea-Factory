from rest_framework import serializers
from .models import TeaLeaves 


class TeaLeavesSerializer(serializers.Serializer):
    class Meta:
        model= TeaLeaves
        fields = ["id", "provider_name", "collected_weight", "any_note" ,"collected_date"]

        