from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User




@api_view(["POST"])
def signin(request):
    return Response(
        data={"message": "Signin API"},
        status=status.HTTP_200_OK
    )    



@api_view(["POST"])
def signup(request):
    return Response(
        data={"message": "Signup API"},
        status=status.HTTP_200_OK
    )  
