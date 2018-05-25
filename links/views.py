from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from links.models import Category, Link
from links.serializers import CategorySerializer, LinksSerializer

class CategoryList(APIView):
    """
    List all categories, or create a new category.
    """
    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetails(APIView):
    """
    Retrieve, update or delete a category instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the Category content along with this pull request
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LinksList(APIView):
    """
    List all links, or create a new category.
    """
    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        links = Link.objects.all()
        serializer = LinksSerializer(links, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = LinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LinksDetails(APIView):
    """
    Retrieve, update or delete a category instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return Link.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the Category content along with this pull request
        """
        links = self.get_object(pk)
        serializer = LinksSerializer(links)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        links = self.get_object(pk)
        serializer = LinksSerializer(links, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        links = self.get_object(pk)
        links.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)