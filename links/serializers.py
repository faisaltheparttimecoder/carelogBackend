from rest_framework import serializers
from links.models import Category, Link


class LinksSerializer(serializers.ModelSerializer):
    """
    Serializer for the Link table
    """
    category_name = serializers.SerializerMethodField('get_category', read_only=True)

    def get_category(self, obj):
        return obj.category_id.name

    class Meta:
        model = Link
        fields = ('id', 'name', 'url', 'info', 'category_id', 'category_name')


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category table
    """

    # Reverse serializer lookup
    category = LinksSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'category')

