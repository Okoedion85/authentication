from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import generics # type: ignore
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class BlogList(generics.ListCreateAPIView):
     queryset = Blog.objects.all()
     serializer_class = BlogSerializer
     permission_classes = [IsAuthenticated] # to make sure users are logged in before they perform this function
     
     
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Blog.objects.all()
     serializer_class = BlogSerializer
     permission_classes = [IsAuthenticated] # to make sure users are logged in before they perform this function