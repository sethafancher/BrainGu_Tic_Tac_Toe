from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetView(APIView):
    
    serializer_class = SnippetSerializer
  
    def get(self, request):
        detail = [
            {"Round": detail.id, "Winner": detail.winner}
        for detail in Snippet.objects.all()
        ]
        return Response(detail)
  
    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return  Response(serializer.data)