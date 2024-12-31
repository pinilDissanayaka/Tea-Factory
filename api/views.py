from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import TeaLeaveSerializer
from rest_framework.views import APIView
from .models import TeaLeaves
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


def index(request):
    return HttpResponse("Test API Server")


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass
    


