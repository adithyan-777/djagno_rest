# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from snippets.models import Snippet
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


# @api_view(["GET", "POST"])
class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create a new snippet.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # def get(self, request, format=None):
    #     snippets = Snippet.objects.all()
    #     serializer = SnippetSerializer(snippets, many=True)
    #     return Response(serializer.data)

    # def post(self, request, format=None):
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "POST", "DELETE"])
# def snippet_detail(request, pk, format=None):
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code snippet.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # def get_object(self, pk):
    #     try:
    #         snippet = Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    #         # return Response(status=status.HTTP_404_NOT_FOUND)

    # def get(self, request, pk, format=None):
    #     snippet = self.get_object(pk=pk)
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk=pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delelte(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     if snippet:
    #         snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
