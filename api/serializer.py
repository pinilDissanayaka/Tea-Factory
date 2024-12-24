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
        fields = ["username", "email", "role", "password"]

        extra_kwargs={
            "password":{"write_only": True}
        }

    def create(self, validated_data):
        user=User.objects.create_user(**validated_data)

        return user


        