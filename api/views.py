from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import TeaLeaveSerializer
from rest_framework.views import APIView
from .models import TeaLeaves
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, Token
from .serializer import UserRegisterSerializer
from django.contrib.auth.models import User
from rest_framework import status




# Create your views here.


def index(request):
    return HttpResponse("Test API Server")


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        request_data=request.data

        serializer=UserRegisterSerializer(data=request_data)

        if serializer.is_valid():
            new_user=serializer.save()

            refresh_token=RefreshToken.for_user(user=new_user)

            return Response({
                "message":"User Created Successfully.",
                "access_token": str(refresh_token.access_token),
                "refresh_taken": str(refresh_token)
            },
            status=status.HTTP_201_CREATED
            )
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        request_data=request.data

        username=request_data.get("username")
        password=request_data.get("password")

        user = User.objects.filter(username=username)

        if user.exists():
            if user.check_password(password):
                refresh_token=RefreshToken.for_user(user=user)
                return Response(
                    {
                        "message":"User Logging Successfully.",
                        "access_token": str(refresh_token.access_token),
                        "refresh_taken": str(refresh_token)
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "message":"Invalid Password"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {
                    "message":"Invalid Username"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

class TeaLeavesView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]


    def get(self, request):
        tealeaves_records=TeaLeaves.objects.all()

        










