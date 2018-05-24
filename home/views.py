from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import generics
from home.models import BcsTeam, MainPage, Certification, Feedback
from home.serializers import BcsTeamSerializer, MainPageSerializer, CertificationSerializer, FeedbackSerializer


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


class CertificationList(APIView):
    """
    List all Certification, or create a new Certification.
    """

    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        certification = Certification.objects.all()
        serializer = CertificationSerializer(certification, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CertificationDetails(APIView):
    """
    Retrieve, update or delete a Certification instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the Certification content along with this pull request
        """
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        certification = self.get_object(pk)
        serializer = CertificationSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        certification = self.get_object(pk)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FeedbackList(APIView):
    """
    List all Feedback, or create a new Feedback.
    """

    def get(self, request, format=None):
        """
        The default get method, i.e on page load
        """
        feedback = Feedback.objects.all()
        serializer = FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        The default post method.
        """
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FeedbackDetails(APIView):
    """
    Retrieve, update or delete a Feedback instance.
    """

    def get_object(self, pk):
        """
        Get the perticular row from the table.
        """
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        We are going to add the Certification content along with this pull request
        """
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        """
        When requested update the corresponding entry of the table
        """
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        When requested delete the corresponding entry of the table
        """
        feedback = self.get_object(pk)
        feedback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


