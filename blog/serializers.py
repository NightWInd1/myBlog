from rest_framework import serializers
from django.utils.html import linebreaks
import re
from .models import Category, Post, Comment


def to_html(value):
    if re.search(r'<[^>]+>', value):
        return value
    return linebreaks(value)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'icon', 'parent')


class CategoryTreeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'icon', 'children')

    def get_children(self, obj):
        children = obj.children.all()
        return CategoryTreeSerializer(children, many=True).data if children else []


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'content', 'created_at')


class PostListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author_name = serializers.CharField(source='author.first_name', read_only=True)
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author_name', 'category_name',
                  'excerpt', 'cover_image', 'is_pinned', 'comment_count',
                  'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['excerpt'] = to_html(data['excerpt'])
        return data

    def get_comment_count(self, obj):
        return obj.comments.count()


class PostDetailSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author_name = serializers.CharField(source='author.first_name', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author_name', 'category_name',
                  'content', 'excerpt', 'cover_image', 'is_pinned',
                  'comments', 'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['content'] = to_html(data['content'])
        data['excerpt'] = to_html(data['excerpt'])
        return data
