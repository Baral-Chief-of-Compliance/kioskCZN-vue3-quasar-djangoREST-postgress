from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from kioskController.models import Post
from kioskController.serializers import PostSerializer



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = '__all__'