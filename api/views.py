from .models import TeaLeaves
from .serializer import TeaLeavesSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', "POST"])
def all_records(request):
    if request.method=="GET":
        data = TeaLeaves.objects.all()

        serialized_data=TeaLeavesSerializer(data, many=True)

        return JsonResponse({"leaves":serialized_data.data}, 
                            safe=False)

    if request.method=="POST":
        serialized_data=TeaLeavesSerializer(data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({serialized_data},
                                status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"status": "error"})




