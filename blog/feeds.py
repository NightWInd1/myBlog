from django.contrib.syndication.views import Feed
from .models import Post
from .serializers import plain_text


class LatestPostsFeed(Feed):
    title = '晚风的博客'
    link = '/'
    description = '记录代码、生活和每一个值得珍藏的瞬间。'

    def items(self):
        return Post.objects.filter(status='published').order_by('-created_at')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return plain_text(item.excerpt or item.content)[:300]

    def item_link(self, item):
        return f'/post/{item.slug}'

    def item_pubdate(self, item):
        return item.created_at
