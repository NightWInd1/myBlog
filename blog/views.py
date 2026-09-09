from rest_framework import generics, pagination
from rest_framework.response import Response
from django.db.models import Q
from .models import Post, Comment, Category
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer, CategoryTreeSerializer


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        qs = Post.objects.filter(status='published')
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(
                Q(category__slug=category) |
                Q(category__parent__slug=category)
            )
        return qs


class PinnedPostView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(status='published', is_pinned=True)[:3]


class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(status='published')
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'


class LatestCommentsView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()[:5]


class LatestPostsView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(status='published')[:5]


class SearchView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        if not q:
            return Post.objects.none()
        return Post.objects.filter(status='published').filter(
            Q(title__icontains=q) | Q(excerpt__icontains=q) | Q(content__icontains=q)
        )


class CategoriesView(generics.ListAPIView):
    serializer_class = CategoryTreeSerializer

    def get_queryset(self):
        return Category.objects.filter(parent__isnull=True, children__isnull=False).distinct()
