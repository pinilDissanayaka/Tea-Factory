from rest_framework import serializers
from .models import TeaLeaves 


class TeaLeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model= TeaLeaves
        fields = "__all__"

        