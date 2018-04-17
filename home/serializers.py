from rest_framework import serializers
from home.models import BcsTeam


class BcsTeamSerializer(serializers.ModelSerializer):
    """
    Serializer for the BcsTeam table
    """
    bcsteam_org_name = serializers.SerializerMethodField('get_bcsteam_org', read_only=True)

    def get_bcsteam_org(self, obj):
        orgs = []
        for i in obj.accounts.get_queryset():
            orgs.append(i.name)
        return orgs

    class Meta:
        model = BcsTeam
        fields = ('id', 'first_name',
                  'last_name',
                  'email',
                  'phone',
                  'region',
                  'role',
                  'slack_handler',
                  'accounts',
                  'location', 'bcsteam_org_name',)

