from rest_framework import serializers
from products.models import Product


class ProductsSerializer(serializers.ModelSerializer):
    """
    Serializer of the Product table.
    """
    class Meta:
        model = Product
        fields = ('id', 'name', 'slug', 'url')
