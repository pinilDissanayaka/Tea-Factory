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
    
    def update(self, instance, validate_data):
        instance.username=validate_data.get('username', instance.username)  



    


class TeaLeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeaLeaves
        fields="__all__"

    def create(self, validated_data):
        new_tea=TeaLeaves.objects.create(
            quality=validated_data.get('quality'),
            quantity=validated_data.get('quantity'),
            description=validated_data.get('description'),
            collector_at=validated_data.get('collector_at'),
            collector_name=validated_data.get('collector_name')
            
        )

        new_tea.save()

        return new_tea