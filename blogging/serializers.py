# from django.contrib.auth.models import User, Group
from blogging.models import Category, Post
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'description']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'category', 'created_date', 'modified_date', 
        'published_date']