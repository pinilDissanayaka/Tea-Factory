from rest_framework.response import Response
from django.http import HttpResponse
from .serializer import TeaLeaveSerializer
from .models import TeaLeaves
from rest_framework.decorators import api_view

# Create your views here.


def index_1(request):
    return HttpResponse("Test API Server")


@api_view(["GET"])
def index(request):
    user=request.user

    print(user)
    return HttpResponse("Test API Server")


