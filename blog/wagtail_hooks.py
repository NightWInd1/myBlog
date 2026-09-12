"""Wagtail 管理后台配置。

这里使用 Wagtail 的 ModelViewSet 管理现有博客模型，避免迁移时复制或删除
文章数据。Vue 前台继续读取原有 REST API，因此后台升级不会改变公开页面。
"""

from wagtail import hooks
from wagtail.admin.viewsets.model import ModelViewSet

from .models import Category, Comment, Post


class PostViewSet(ModelViewSet):
    model = Post
    name = 'posts'
    menu_label = '文章'
    menu_icon = 'doc-full'
    menu_order = 100
    add_to_admin_menu = True
    list_display = ('title', 'category', 'status', 'is_pinned', 'updated_at')
    list_filter = ('status', 'is_pinned', 'category', 'created_at')
    search_fields = ('title', 'slug', 'content', 'excerpt')
    ordering = ('-is_pinned', '-created_at')
    inspect_view_enabled = True
    form_fields = (
        'title',
        'slug',
        'author',
        'category',
        'status',
        'is_pinned',
        'content',
        'excerpt',
        'cover_image',
    )


class CategoryViewSet(ModelViewSet):
    model = Category
    name = 'categories'
    menu_label = '分类'
    menu_icon = 'folder-open-inverse'
    menu_order = 110
    add_to_admin_menu = True
    list_display = ('name', 'slug', 'parent', 'icon')
    list_filter = ('parent',)
    search_fields = ('name', 'slug', 'description')
    ordering = ('name',)
    inspect_view_enabled = True
    form_fields = ('name', 'slug', 'parent', 'description', 'icon')


class CommentViewSet(ModelViewSet):
    model = Comment
    name = 'comments'
    menu_label = '评论'
    menu_icon = 'comment'
    menu_order = 120
    add_to_admin_menu = True
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author_name', 'email', 'content', 'post__title')
    ordering = ('-created_at',)
    inspect_view_enabled = True
    form_fields = ('post', 'author_name', 'email', 'content')


@hooks.register('register_admin_viewset')
def register_post_viewset():
    return PostViewSet('post')


@hooks.register('register_admin_viewset')
def register_category_viewset():
    return CategoryViewSet('category')


@hooks.register('register_admin_viewset')
def register_comment_viewset():
    return CommentViewSet('comment')
