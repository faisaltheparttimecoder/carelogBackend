import feedparser
from security.models import RssFeed
from security.serializers import RssFeedSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RssFeedList(APIView):
    """
    List all rssfeed, or create a new rssfeed.
    """
    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        rssfeed = RssFeed.objects.all()
        serializer = RssFeedSerializer(rssfeed, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = RssFeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RssFeedDetails(APIView):
    """
    Retrieve, update or delete a rssfeed instance.
    """

    def get_feedcontent(self, url):
        """
        Get Rss content of the selected item
        """
        try:
            return feedparser.parse(url)['entries']
        except Exception as e:
            return []

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return RssFeed.objects.get(pk=pk)
        except RssFeed.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the RSS feed content along with this pull request
        """
        rssfeed = self.get_object(pk)
        serializer = RssFeedSerializer(rssfeed)
        data = serializer.data
        data['content'] = self.get_feedcontent(serializer.data['url'])
        return Response(data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        rssfeed = self.get_object(pk)
        serializer = RssFeedSerializer(rssfeed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        rssfeed = self.get_object(pk)
        rssfeed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)