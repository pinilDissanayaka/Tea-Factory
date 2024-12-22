from .models import TeaLeaves
from .serializer import TeaLeavesSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET', "POST"])
def all_records(request):
    """
    Handle GET and POST requests for all leaves records.

    If the request method is GET, retrieve all records from the database
    and serialize the data. Return a JsonResponse with the serialized data.

    If the request method is POST, serialize the data from the request body
    and validate the data. If the data is valid, save the data to the database
    and return a JsonResponse with the serialized data and a status code of 201
    Created. If the data is not valid, return a JsonResponse with an error status.

    Parameters
    ----------
    request : HttpRequest
        The request object.

    Returns
    -------
    JsonResponse
        The response object.
    """
    if request.method=="GET":
        # Retrieve all records from the database
        data = TeaLeaves.objects.all()

        # Serialize the data
        serialized_data=TeaLeavesSerializer(data, many=True)

        # Return a JsonResponse with the serialized data
        return JsonResponse({"leaves":serialized_data.data}, 
                            safe=False)

    if request.method=="POST":
        # Serialize the data from the request body
        serialized_data=TeaLeavesSerializer(data=request.data)

        # Validate the data
        if serialized_data.is_valid():
            # Save the data to the database
            serialized_data.save()

            # Return a JsonResponse with the serialized data and a status code of 201 Created
            return JsonResponse({serialized_data},
                                status=status.HTTP_201_CREATED)
        else:
            # Return a JsonResponse with an error status
            return JsonResponse({"status": "error"})




