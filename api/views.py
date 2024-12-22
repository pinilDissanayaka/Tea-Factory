from rest_framework import generics
from .models import TeaLeaves
from .serializer import TeaLeavesSerializer




class TeaLeavesCreate(generics.ListCreateAPIView):
    queryset=TeaLeaves.objects.all()
    serializer_class=TeaLeavesSerializer


