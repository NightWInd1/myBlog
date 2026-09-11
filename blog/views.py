from collections import defaultdict

from django.db.models import Count, Q
from django.db.models.functions import TruncMonth
from rest_framework import generics, pagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment, Category
from .serializers import PostListSerializer, PostDetailSerializer, CommentSerializer, CategoryTreeSerializer


def published_posts():
    return Post.objects.filter(status='published').select_related('author', 'category').annotate(comment_count=Count('comments')).order_by('-is_pinned', '-created_at', '-pk')


def category_ids(slug):
    categories = list(Category.objects.values('id', 'slug', 'parent_id'))
    selected = {c['id'] for c in categories if c['slug'] == slug}
    frontier = selected.copy()
    while frontier:
        frontier = {c['id'] for c in categories if c['parent_id'] in frontier} - selected
        selected.update(frontier)
    return selected


class StandardPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        qs = published_posts()
        category = self.request.query_params.get('category')
        if category:
            qs = qs.filter(category_id__in=category_ids(category))
        if self.request.query_params.get('ordering') == 'latest':
            qs = qs.order_by('-created_at', '-pk')
        return qs


class PinnedPostView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return published_posts().filter(is_pinned=True)[:3]


class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return published_posts().prefetch_related('comments__post')


class LatestCommentsView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post__status='published').select_related('post')[:5]


class LatestPostsView(generics.ListAPIView):
    serializer_class = PostListSerializer

    def get_queryset(self):
        return published_posts().order_by('-created_at', '-pk')[:5]


class SearchView(generics.ListAPIView):
    serializer_class = PostListSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        q = self.request.query_params.get('q', '').strip()
        if not q:
            return Post.objects.none()
        return published_posts().filter(Q(title__icontains=q) | Q(excerpt__icontains=q) | Q(content__icontains=q))


class CategoriesView(APIView):
    def get(self, request):
        categories = list(Category.objects.annotate(direct_count=Count('post', filter=Q(post__status='published'))))
        children = defaultdict(list)
        for category in categories:
            children[category.parent_id].append(category)
        counts = {}

        def count_posts(category, visited):
            if category.id in visited:
                return 0
            total = category.direct_count + sum(count_posts(child, visited | {category.id}) for child in children[category.id])
            counts[category.id] = total
            return total

        for root in children[None]:
            count_posts(root, set())
        return Response(CategoryTreeSerializer(children[None], many=True, context={'children': children, 'counts': counts}).data)


class SiteStatsView(APIView):
    def get(self, request):
        posts = Post.objects.filter(status='published')
        return Response({
            'posts': posts.count(),
            'categories': Category.objects.count(),
            'comments': Comment.objects.filter(post__status='published').count(),
            'last_updated': posts.order_by('-updated_at').values_list('updated_at', flat=True).first(),
        })


class ArchivesView(APIView):
    def get(self, request):
        posts = Post.objects.filter(status='published').select_related('category').order_by('-created_at', '-pk')
        return Response({
            'months': list(posts.order_by().annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('-month')),
            'posts': list(posts.values('id', 'title', 'slug', 'created_at', 'category__name')),
        })
