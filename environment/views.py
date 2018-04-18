from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from environment.models import AccountInformation, ContactInformation, EnvironmentNote
from environment.serializers import AccountInformationSerializer, ContactInformationSerializer, EnvironmentNotesSerializer


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
        Get the particular row from the table.
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
        print(request.data)
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


class ContactInformationList(generics.ListAPIView):
    """
    List all ContactInformation, or create a new ContactInformation.
    """

    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('org_id', 'id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = ContactInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactInformationDetails(APIView):
    """
    Retrieve, update or delete a ContactInformation instance.
    """

    def get_object(self, pk):
        """
        Get the particular row from the table.
        """
        try:
            return ContactInformation.objects.get(pk=pk)
        except ContactInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the contact info content along with this pull request
        """
        contact_info = self.get_object(pk)
        serializer = ContactInformationSerializer(contact_info)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        contact_info = self.get_object(pk)
        serializer = ContactInformationSerializer(contact_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        contact_info = self.get_object(pk)
        contact_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EnvironmentNotesList(generics.ListAPIView):
    """
    List all EnvironmentNotes, or create a new EnvironmentNotes.
    """

    queryset = EnvironmentNote.objects.all()
    serializer_class = EnvironmentNotesSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('org_id', 'id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = EnvironmentNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnvironmentNotesDetails(APIView):
    """
    Retrieve, update or delete a EnvironmentNotes instance.
    """

    def get_object(self, pk):
        """
        Get the particular row from the table.
        """
        try:
            return EnvironmentNote.objects.get(pk=pk)
        except EnvironmentNote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the contact info content along with this pull request
        """
        env_notes = self.get_object(pk)
        serializer = EnvironmentNotesSerializer(env_notes)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        env_info = self.get_object(pk)
        serializer = EnvironmentNotesSerializer(env_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        env_info = self.get_object(pk)
        env_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)