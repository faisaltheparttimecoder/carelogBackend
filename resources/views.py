from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from resources.models import Resource
from resources.serializers import ResourceSerializer


class ResourceList(APIView):
    """
    List all Feedback, or create a new Feedback.
    """

    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        resource = Resource.objects.all()
        serializer = ResourceSerializer(resource, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourceDetails(APIView):
    """
    Retrieve, update or delete a Resource instance.
    """

    def get_object(self, pk):
        """
        Get the particular row from the table.
        """
        try:
            return Resource.objects.get(pk=pk)
        except Resource.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the Certification content along with this pull request
        """
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        resource = self.get_object(pk)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        resource = self.get_object(pk)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
