import math
import re
from html import unescape

from django.utils.html import linebreaks, strip_tags
from rest_framework import serializers

from .models import Category, Post, Comment


def plain_text(value):
    value = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', value, flags=re.S | re.I)
    return re.sub(r'\s+', ' ', unescape(strip_tags(value))).strip()


def to_html(value):
    if re.search(r'<[^>]+>', value):
        return value
    return linebreaks(value, autoescape=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'description', 'icon', 'parent')


class CategoryTreeSerializer(CategorySerializer):
    children = serializers.SerializerMethodField()
    post_count = serializers.SerializerMethodField()

    class Meta(CategorySerializer.Meta):
        fields = CategorySerializer.Meta.fields + ('children', 'post_count')

    def get_children(self, obj):
        return CategoryTreeSerializer(self.context['children'].get(obj.id, []), many=True, context=self.context).data

    def get_post_count(self, obj):
        return self.context['counts'].get(obj.id, 0)


class CommentSerializer(serializers.ModelSerializer):
    post_slug = serializers.CharField(source='post.slug', read_only=True)
    post_title = serializers.CharField(source='post.title', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author_name', 'content', 'created_at', 'post_slug', 'post_title')


class PostListSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True, default='未分类')
    category_slug = serializers.CharField(source='category.slug', read_only=True, default='')
    author_name = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(read_only=True)
    reading_minutes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'slug', 'author_name', 'category_name', 'category_slug',
                  'excerpt', 'cover_image', 'is_pinned', 'comment_count', 'reading_minutes',
                  'created_at', 'updated_at')

    def get_author_name(self, obj):
        return obj.author.first_name or obj.author.username

    def get_reading_minutes(self, obj):
        return max(1, math.ceil(len(plain_text(obj.content)) / 400))

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['excerpt'] = plain_text(instance.excerpt or instance.content)[:180]
        return data


class PostDetailSerializer(PostListSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta(PostListSerializer.Meta):
        fields = PostListSerializer.Meta.fields + ('content', 'comments')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['content'] = to_html(instance.content)
        return data
