from rest_framework import serializers
from environment.models import AccountInformation, ContactInformation, EnvironmentNote, EnvironmentProductsList
from environment.models import EnvironmentType, EnvironmentInstance, EnvironmentInstanceProduct


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


class EnvironmentNotesSerializer(serializers.ModelSerializer):
    """
    Serializer for the EnvironmentNotes table
    """
    class Meta:
        model = EnvironmentNote
        fields = '__all__'


class EnvironmentProductsListSerializer(serializers.ModelSerializer):
    """
    Serializer for the EnvironmentProductsList table
    """

    environment_product_list = serializers.SerializerMethodField('get_product_list', read_only=True)

    def get_product_list(self, obj):
        products = []
        for i in obj.products.get_queryset():
            products.append(i.name)
        return products

    class Meta:
        model = EnvironmentProductsList
        fields = ('id',
                  'org_id',
                  'products',
                  'environment_product_list',)


class EnvironmentTypeSerializer(serializers.ModelSerializer):
    """
    Serializer for the EnvironmentType table
    """
    class Meta:
        model = EnvironmentType
        fields = '__all__'


class EnvironmentInstanceProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the EnvironmentInstanceProducts table
    """
    class Meta:
        model = EnvironmentInstanceProduct
        fields = '__all__'


class EnvironmentInstanceSerializer(serializers.ModelSerializer):
    """
    Serializer for the EnvironmentInstance table
    """
    environment_instance = EnvironmentInstanceProductSerializer(many=True, read_only=True)
    environment_type = serializers.SerializerMethodField('get_type_environment', read_only=True)

    def get_type_environment(self, obj):
        return obj.type_id.type

    class Meta:
        model = EnvironmentInstance
        fields = ('id', 'type_id', 'org_id', 'name', 'infrastructure', 'updated', 'timeline_id',
                  'environment_type', 'environment_instance')

