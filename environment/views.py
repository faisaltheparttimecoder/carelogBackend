from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from environment.models import AccountInformation
from environment.serializers import AccountInformationSerializer


class AccountInformationList(generics.ListAPIView):
    """
    List all AccountInformation, or create a new AccountInformation.
    """

    queryset = AccountInformation.objects.all()
    serializer_class = AccountInformationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('org_id', 'id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = AccountInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountInformationDetails(APIView):
    """
    Retrieve, update or delete a AccountInformation instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return AccountInformation.objects.get(pk=pk)
        except AccountInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the account info content along with this pull request
        """
        account_info = self.get_object(pk)
        serializer = AccountInformationSerializer(account_info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        account_info = self.get_object(pk)
        serializer = AccountInformationSerializer(account_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        account_info = self.get_object(pk)
        account_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)