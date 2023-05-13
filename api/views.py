from django.shortcuts import render
from blog.models import Post
from rest_framework.generics import ListAPIView
from .serializers import PostListAPIView
# Create your views here.


class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListAPIView
