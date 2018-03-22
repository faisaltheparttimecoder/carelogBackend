import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from common.utilities import get_url
from zendesk.models import Organisation
from zendesk.serializers import OrganisationSerializer


class ZendeskSearch(APIView):
    """
    Custom Serializer for zendesk search API.
    """
    def get(self, request, search_string , format=None):
        """
        The default get method, i.e on page load
        """
        search_api = 'https://discuss.zendesk.com/api/v2/search?' + search_string + '*'
        return Response(get_url(search_api, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD']))


class OrganisationList(APIView):
    """
    List all Organisation, or create a new Organisation.
    """
    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        org = Organisation.objects.all()
        serializer = OrganisationSerializer(org, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = OrganisationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganisationDetails(APIView):
    """
    Retrieve, update or delete a Organisation instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return Organisation.objects.get(pk=pk)
        except Organisation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the RSS feed content along with this pull request
        """
        org = self.get_object(pk)
        serializer = OrganisationSerializer(org)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        org = self.get_object(pk)
        serializer = OrganisationSerializer(org, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        org = self.get_object(pk)
        org.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
