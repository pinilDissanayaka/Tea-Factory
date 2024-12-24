from .models import TeaLeaves
from .serializer import TeaLeavesSerializer, UserSerializer
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
            return JsonResponse(data={serialized_data},
                                status=status.HTTP_201_CREATED)
        else:
            # Return a JsonResponse with an error status
            return JsonResponse(data={"status": "error"},
                                status=status.HTTP_404_NOT_FOUND)
        

@api_view(["GET", "DELETE"])
def single_record(request, user):

    """
    A view that handles GET and DELETE requests to retrieve or delete a single record from the database.

    Parameters
    ----------
    request : HttpRequest
        The request object.
    user : str
        The provider_name of the record to be retrieved or deleted.

    Returns
    -------
    JsonResponse
        The response object. If the request is GET, it contains the serialized record.
        If the request is DELETE, it contains a success message.
        If the record is not found, it contains an error message.
    """
    try:
        # Retrieve the record with the given id from the database
        record = TeaLeaves.objects.filter(provider_name=user)
    except TeaLeaves.DoesNotExist:
        # Return a JsonResponse with an error status if the record is not found
        return JsonResponse({"status": "Record Not Found 3"},
                            status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        # Serialize the record
        serialized_record=TeaLeavesSerializer(record, many=True)

        return JsonResponse(
                serialized_record.data,
                safe=False,
                status=status.HTTP_200_OK
        )
    elif request.method == "DELETE":
        # Delete the record from the database
        record.delete()
        # Return a JsonResponse with a status code of 202 Accepted
        return JsonResponse(
            data={"Deleted"},
            status=status.HTTP_202_ACCEPTED,
            safe=False
            )
    else:
         return JsonResponse(
            {"status": "Method Not Allowed"},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )







