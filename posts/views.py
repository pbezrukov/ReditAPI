from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


class PostsView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(data=serializer.data)
