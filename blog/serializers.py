from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):


    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'created_at']