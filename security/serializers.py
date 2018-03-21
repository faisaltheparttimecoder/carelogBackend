from rest_framework import serializers
from security.models import RssFeed


class RssFeedSerializer(serializers.ModelSerializer):
    """
    Serializer for the RssFeed table
    """
    class Meta:
        model = RssFeed
        fields = ('id', 'name', 'url')
