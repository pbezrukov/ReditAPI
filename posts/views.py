from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .pagiantor import PostsPaginator
from .models import Post
from .serializers import PostSerializer


class PostsView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PostsPaginator


class OnePostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
