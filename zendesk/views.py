import os
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from django.http import Http404
from common.utilities import get_url
from zendesk.models import Organisation, TicketNote, HotTicket
from zendesk.serializers import OrganisationSerializer, TicketNoteSerializer, HotTicketsSerializer
from zendesk.lib.extract_hot_tickets import extract_hot_ticket


class ZendeskSearch(APIView):
    """
    Custom Serializer for zendesk search API.
    """
    def get(self, request, search_string , format=None):
        """
        The default get method, i.e on page load
        """
        search_api = os.environ['ZENDESK_BASE_URL'] + '/api/v2/search?' + search_string
        if search_string.startswith('query=type:ticket organization:'):
            zd_data = get_url(search_api, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD'])
            zd_data['hot_tickets'] = extract_hot_ticket(search_string)
            return Response(zd_data)
        else:
            return Response(get_url(search_api, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD']))


class ZendeskTicketComments(APIView):
    """
    Custom serializer from Zendesk Ticket Audits
    """
    def get(self, request, ticket , format=None):
        """
        Send ticket audits based on ticket non
        """
        audit_api = os.environ['ZENDESK_BASE_URL'] + '/api/v2/tickets/' + ticket + '/comments.json?include=users&sort_order=desc'
        return Response(get_url(audit_api, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD']))


class ZendeskTicketMetrics(APIView):
    """
    Custom serializer from Zendesk Ticket Audits
    """
    def get(self, request, ticket , format=None):
        """
        Send ticket audits based on ticket non
        """
        audit_api = os.environ['ZENDESK_BASE_URL'] + '/api/v2/tickets/' + ticket + '/metrics.json'
        return Response(get_url(audit_api, os.environ['ZENDESK_USERNAME'], os.environ['ZENDESK_PASSWORD']))


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


class TicketNoteList(generics.ListAPIView):
    """
    List all TicketNote, or create a new TicketNote.
    """

    queryset = TicketNote.objects.all()
    serializer_class = TicketNoteSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('ticket_id', 'org_id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = TicketNoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketNoteDetails(APIView):
    """
    Retrieve, update or delete a TicketNote instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return TicketNote.objects.get(pk=pk)
        except TicketNote.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HotTicketsList(generics.ListAPIView):
    """
    List all TicketNote, or create a new HotTicket.
    """

    queryset = HotTicket.objects.all()
    serializer_class = HotTicketsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('ticket_id', 'org_id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = HotTicketsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotTicketDetails(APIView):
    """
    Retrieve, update or delete a HotTicket instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return HotTicket.objects.get(ticket_id=pk)
        except HotTicket.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        hot = self.get_object(pk)
        hot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
