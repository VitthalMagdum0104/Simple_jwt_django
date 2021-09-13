from blog.serializers import BlogSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Blog
from .serializers import BlogSerializer
# Create your views here.


class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CreateBlog(APIView):
    permission_classes = [IsAuthenticated]

    def get(slef, request):
        blog = Blog.objects.filter(created_by=request.user.id)
        blog_serializer = BlogSerializer(blog, many=True)
        return Response(blog_serializer.data)

    def post(self, request):
        data = JSONParser().parse(request)
        title = data['title']
        content = data['content']
        slug = data['slug']
        print(request.user.id)

        blog = Blog.objects.create(
            title=title, content=content, slug=slug, created_by=request.user)

        return Response({'message': 'Blog created successfully.'})


class RetrieveUpdateView(RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DestroyView(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
