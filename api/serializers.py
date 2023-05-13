from rest_framework.serializers import ModelSerializer
from blog.models import Post
class PostListAPIView(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title','author','body']


class PostDetailAPIView(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'body']

