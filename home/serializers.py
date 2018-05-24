from rest_framework import serializers
from home.models import BcsTeam, MainPage, Certification, Feedback


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


class MainPageSerializer(serializers.ModelSerializer):
    """
    Serializer for the MainPage table
    """

    class Meta:
        model = MainPage
        fields = '__all__'


class CertificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Certification table
    """
    bcs_team_achievement = serializers.SerializerMethodField('get_bcs_team', read_only=True)

    def get_bcs_team(self, obj):
        return obj.team_id.first_name + ' ' + obj.team_id.last_name

    class Meta:
        model = Certification
        fields = ('id', 'team_id', 'certification', 'bcs_team_achievement',)


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Feedback table
    """

    class Meta:
        model = Feedback
        fields = '__all__'

