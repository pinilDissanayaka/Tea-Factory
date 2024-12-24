from .models import TeaLeaves
from .serializer import TeaLeavesSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status




class ProductAPIViewInfo(APIView):
    def get(self, request):
        """A view that handles GET requests to retrieve a list of records from the database.

        Parameters
        ----------
        request : HttpRequest
            The request object.

        Returns
        -------
        JsonResponse
            The response object containing the serialized list of records.
        """
        # Retrieve all records from the database
        data = TeaLeaves.objects.all()
        # Serialize the records
        serialized_data = TeaLeavesSerializer(data, many=True)
        # Return a JsonResponse containing the serialized records
        return JsonResponse({"leaves": serialized_data.data}, safe=False)
        

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







