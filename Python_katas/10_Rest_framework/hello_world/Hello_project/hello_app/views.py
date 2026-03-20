from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView

# Create your views here.

class HelloView(APIView):
    """
    A simple API view that returns a greeting message.
    """

    def get(self, request):
        return Response({"message": "Hello, World!"})