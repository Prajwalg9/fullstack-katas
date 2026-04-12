from rest_framework.viewsets import ModelViewSet
from ..models import Posts
from .serializers import PostSerializers

class PostViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializers
    