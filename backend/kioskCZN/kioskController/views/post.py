from rest_framework import viewsets

from kioskController.models import Post
from kioskController.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer