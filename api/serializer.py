from rest_framework import serializers
from django.contrib.auth.models import User
from .models import TeaLeaves



class UserRegisterSerializer(serializers.ModelSerializer):
    conform_password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=["username", "email", "password", "conform_password"]


    def validate(self, attrs):
        if attrs["password"] != attrs["conform_password"]:
            raise serializers.ValidationError("password not match")
        return attrs

    def create(self, validate_data):
        new_user =User.objects.create_user(
            username=validate_data.get('username'),
            email=validate_data.get('email'),
            password=validate_data.get('password')
        )

        new_user.save()

        return new_user



    


class TeaLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeaLeaves
        fields="__all__"

