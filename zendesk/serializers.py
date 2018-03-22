from rest_framework import serializers
from zendesk.models import Organisation


class OrganisationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Organization table
    """
    class Meta:
        model = Organisation
        fields = ('id', 'org_id', 'name', 'created_at', 'location', 'expired_contract')



