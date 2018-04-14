from rest_framework import serializers
from environment.models import AccountInformation


class AccountInformationSerializer(serializers.ModelSerializer):
    """
    Serializer for the AccountInformation table
    """
    class Meta:
        model = AccountInformation
        fields = '__all__'
