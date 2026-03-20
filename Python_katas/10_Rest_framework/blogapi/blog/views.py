from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .permissions import IsPostProcessor
from rest_framework import filters

# Create your views here.

class PostViewSet(ModelViewSet):
    """
    A viewset for viewing and editing blog posts.
    """
    permission_classes = [IsAuthenticated,IsPostProcessor]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'created_by__username']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']