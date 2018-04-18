from rest_framework import serializers
from environment.models import AccountInformation, ContactInformation


class AccountInformationSerializer(serializers.ModelSerializer):
    """
    Serializer for the AccountInformation table
    """
    class Meta:
        model = AccountInformation
        fields = '__all__'


class ContactInformationSerializer(serializers.ModelSerializer):
    """
    Serializer for the ContactInformation table
    """
    class Meta:
        model = ContactInformation
        fields = '__all__'
