from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from timeline.models import Timeline, TimelineDetail, TimelineCategory
from timeline.serializers import TimelineSerializer, TimelineCategorySerializer, TimelineDetailSerializer


class TimelineList(generics.ListAPIView):
    """
    List all Timeline, or create a new Timeline.
    """

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('title', 'org_id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = TimelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimelineDetails(APIView):
    """
    Retrieve, update or delete a Timeline instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return Timeline.objects.get(pk=pk)
        except Timeline.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the timeline content along with this pull request
        """
        timeline = self.get_object(pk)
        serializer = TimelineSerializer(timeline)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        timeline = self.get_object(pk)
        serializer = TimelineSerializer(timeline, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        timeline = self.get_object(pk)
        timeline.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TimelineCategoryList(generics.ListAPIView):
    """
    List all Timeline category, or create a new Timeline Category.
    """

    queryset = TimelineCategory.objects.all()
    serializer_class = TimelineCategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)


class TimelineDetailList(generics.ListAPIView):
    """
    List all Timeline Detail, or create a new Timeline Detail.
    """

    queryset = TimelineDetail.objects.all()
    serializer_class = TimelineDetailSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('org_id', 'timeline_id')

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = TimelineDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TimelineDetailDetails(APIView):
    """
    Retrieve, update or delete a Timeline Detail instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return TimelineDetail.objects.get(pk=pk)
        except TimelineDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the Timeline Detail content along with this pull request
        """
        timeline_details = self.get_object(pk)
        serializer = TimelineDetailSerializer(timeline_details)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        timeline_details = self.get_object(pk)
        serializer = TimelineDetailSerializer(timeline_details, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        timeline_details = self.get_object(pk)
        timeline_details.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
