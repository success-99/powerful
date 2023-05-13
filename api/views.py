from django.shortcuts import render
from blog.models import Post
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import permissions

from .serializers import PostListAPIView,PostDetailAPIView
# Create your views here.

class PostList(APIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Post.objects.all()
    serializer_class = PostListAPIView

class PostDetail(APIView):
    permission_classes = (permissions.AllowAny,)

    queryset = Post.objects.all()
    serializer_class = PostDetailAPIView

