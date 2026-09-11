from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from .models import Category, Comment, Post


class PublicBlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = get_user_model().objects.create_user(username='writer', first_name='作者')
        cls.root = Category.objects.create(name='技术', slug='tech')
        cls.child = Category.objects.create(name='前端', slug='frontend', parent=cls.root)
        cls.leaf = Category.objects.create(name='Vue', slug='vue', parent=cls.child)
        cls.empty = Category.objects.create(name='生活', slug='life')
        cls.old = Post.objects.create(title='旧置顶文章', slug='pinned', author=cls.author, category=cls.root, content='旧文章', status='published', is_pinned=True, created_at=timezone.now() - timedelta(days=3))
        cls.new = Post.objects.create(title='Vue 实践', slug='vue-guide', author=cls.author, category=cls.leaf, content='<h2>开始</h2><p>学习 Vue &amp; Django</p>', status='published')
        cls.draft = Post.objects.create(title='未公开计划', slug='draft', author=cls.author, category=cls.leaf, content='秘密', status='draft')
        Comment.objects.create(post=cls.new, author_name='读者', content='公开留言')
        Comment.objects.create(post=cls.draft, author_name='作者', content='私有留言')

    def get_json(self, path):
        response = self.client.get(path)
        self.assertEqual(response.status_code, 200)
        return response.json()

    def test_category_tree_counts_and_standalone_roots(self):
        tree = self.get_json('/api/categories/')
        root = next(c for c in tree if c['slug'] == 'tech')
        self.assertEqual(root['post_count'], 2)
        self.assertEqual(root['children'][0]['children'][0]['post_count'], 1)
        self.assertIn('life', [c['slug'] for c in tree])

    def test_parent_filter_includes_all_descendants_and_no_drafts(self):
        data = self.get_json('/api/posts/?category=tech')
        self.assertEqual(data['count'], 2)
        self.assertEqual([p['slug'] for p in data['results']], ['pinned', 'vue-guide'])

    def test_latest_order_is_independent_of_pinning(self):
        self.assertEqual(self.get_json('/api/posts/latest/')[0]['slug'], 'vue-guide')
        self.assertEqual(self.get_json('/api/posts/?ordering=latest')['results'][0]['slug'], 'vue-guide')

    def test_excerpt_fallback_and_reading_metadata(self):
        post = self.get_json('/api/posts/vue-guide/')
        self.assertIn('Vue & Django', post['excerpt'])
        self.assertNotIn('<', post['excerpt'])
        self.assertEqual(post['reading_minutes'], 1)
        self.assertEqual(post['category_slug'], 'vue')
        self.assertEqual(post['comment_count'], 1)
        self.assertIn('<h2>', post['content'])
        self.assertEqual(self.client.get('/api/posts/draft/').status_code, 404)

    def test_public_widgets_do_not_expose_drafts(self):
        comments = self.get_json('/api/comments/latest/')
        self.assertEqual(len(comments), 1)
        self.assertEqual(comments[0]['post_slug'], 'vue-guide')
        stats = self.get_json('/api/stats/')
        self.assertEqual(stats['posts'], 2)
        self.assertEqual(stats['comments'], 1)
        self.assertEqual(stats['categories'], 4)
        archives = self.get_json('/api/archives/')
        self.assertEqual([p['slug'] for p in archives['posts']], ['vue-guide', 'pinned'])
        self.assertEqual(sum(month['count'] for month in archives['months']), 2)

    def test_search_and_pagination(self):
        data = self.get_json('/api/posts/search/?q=Vue&page_size=1')
        self.assertEqual(data['count'], 1)
        self.assertEqual(data['results'][0]['slug'], 'vue-guide')
        self.assertEqual(self.get_json('/api/posts/search/?q=%20')['count'], 0)
        page = self.get_json('/api/posts/?page_size=1')
        self.assertIsNotNone(page['next'])
        self.assertEqual(self.get_json('/api/posts/?page_size=1&page=2')['results'][0]['slug'], 'vue-guide')

    def test_rss_is_xml_with_public_article_links(self):
        response = self.client.get('/feed/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('xml', response['Content-Type'])
        self.assertContains(response, '/post/vue-guide')
        self.assertNotContains(response, '/post/draft')
