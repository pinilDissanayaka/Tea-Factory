from rest_framework import serializers
from .models import TeaLeaves 
from django.contrib.auth.models import User


class TeaLeavesSerializer(serializers.ModelSerializer):
    class Meta:
        model= TeaLeaves
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]

        extra_kwargs={
            "password":{"write_only": True}
        }

    def create(self, validate_data):
        new_user=User.objects.create_user(**validate_data)
        return new_user

        