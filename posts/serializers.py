from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    counter = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ("id", "text", "created_at")
