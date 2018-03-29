from rest_framework import serializers
from timeline.models import Timeline, TimelineCategory, TimelineDetail


class TimelineSerializer(serializers.ModelSerializer):
    """
    Serializer for the Timeline table
    """
    class Meta:
        model = Timeline
        fields = '__all__'


class TimelineCategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Timeline Category table
    """
    class Meta:
        model = TimelineCategory
        fields = '__all__'


class TimelineDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for the TimelineDetail table
    """
    category_color = serializers.SerializerMethodField('get_color', read_only=True)
    category_icon = serializers.SerializerMethodField('get_icon', read_only=True)

    def get_color(self, obj):
        return obj.category_id.color

    def get_icon(self, obj):
        return obj.category_id.icon

    class Meta:
        model = TimelineDetail
        fields = ('id', 'timeline_id', 'org_id', 'category_id', 'created', 'title', 'description', 'category_color', 'category_icon')
