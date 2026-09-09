from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Category, Post, Comment


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(config_name='default'), label='正文')

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'author', 'category', 'status', 'is_pinned', 'created_at')
    list_filter = ('status', 'is_pinned', 'category', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

    fieldsets = (
        ('基本信息', {'fields': ('title', 'slug', 'author', 'category', 'status', 'is_pinned')}),
        ('内容', {'fields': ('content', 'excerpt', 'cover_image')}),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'post', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('author_name', 'content')
