from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .pagiantor import PostsPaginator
from .models import Post
from .serializers import PostSerializer


class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostsPaginator


class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
