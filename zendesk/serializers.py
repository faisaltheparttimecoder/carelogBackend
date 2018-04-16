from rest_framework import serializers
from zendesk.models import Organisation, HotTicket, TicketNote


class OrganisationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Organization table
    """
    class Meta:
        model = Organisation
        fields = ('id', 'org_id',
                  'name', 'created_at',
                  'location', 'expired_contract',
                  'recently_added', 'country',
                  'archived', 'archived_date')


class TicketNoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Organization table
    """

    class Meta:
        model = TicketNote
        fields = ('id', 'ticket_id', 'org_id', 'author', 'created', 'notes')


class HotTicketsSerializer(serializers.ModelSerializer):
    """
    Serializer for the HotTickets table
    """

    class Meta:
        model = HotTicket
        fields = ('id', 'ticket_id', 'org_id', 'hot')



