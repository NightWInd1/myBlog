from django.urls import path
from . import views
from .feeds import LatestPostsFeed

urlpatterns = [
    path('feed/', LatestPostsFeed(), name='post-feed'),
    path('api/stats/', views.SiteStatsView.as_view(), name='site-stats'),
    path('api/archives/', views.ArchivesView.as_view(), name='archives'),
    path('api/posts/', views.PostListView.as_view(), name='post-list'),
    path('api/posts/pinned/', views.PinnedPostView.as_view(), name='post-pinned'),
    path('api/posts/latest/', views.LatestPostsView.as_view(), name='post-latest'),
    path('api/posts/search/', views.SearchView.as_view(), name='post-search'),
    path('api/posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('api/comments/latest/', views.LatestCommentsView.as_view(), name='comment-latest'),
    path('api/categories/', views.CategoriesView.as_view(), name='category-tree'),
]
