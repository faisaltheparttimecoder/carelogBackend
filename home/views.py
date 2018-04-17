from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics
from home.models import BcsTeam, MainPage
from home.serializers import BcsTeamSerializer, MainPageSerializer



class BcsTeamList(APIView):
    """
    List all BcsTeam, or create a new BcsTeam.
    """

    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        team = BcsTeam.objects.all()
        serializer = BcsTeamSerializer(team, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = BcsTeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BcsTeamDetails(APIView):
    """
    Retrieve, update or delete a BcsTeam instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return BcsTeam.objects.get(pk=pk)
        except BcsTeam.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the BcsTeam content along with this pull request
        """
        bcs_team = self.get_object(pk)
        serializer = BcsTeamSerializer(bcs_team)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        bcs_team = self.get_object(pk)
        serializer = BcsTeamSerializer(bcs_team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        bcs_team = self.get_object(pk)
        bcs_team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MainPageList(generics.ListAPIView):
    """
    List all MainPage, or create a new MainPage.
    """

    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('page',)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = MainPageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MainPageDetails(APIView):
    """
    Retrieve, update or delete a MainPage instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return MainPage.objects.get(pk=pk)
        except MainPage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the MainPage content along with this pull request
        """
        main = self.get_object(pk)
        serializer = MainPageSerializer(main)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        main = self.get_object(pk)
        serializer = MainPageSerializer(main, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        main = self.get_object(pk)
        main.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)