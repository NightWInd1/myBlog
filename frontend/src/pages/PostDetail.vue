<template>
  <div class="site-shell">
    <ScrollGradient />
    <Header />
    <main class="page-main" v-if="post">
      <div class="container">
        <article class="post-detail">
          <header class="post-header">
            <div class="post-category">{{ post.category_name }}</div>
            <h1>{{ post.title }}</h1>
            <div class="post-meta">
              <span>{{ post.author_name }}</span>
              <span class="meta-dot">·</span>
              <span>{{ formatWeekday(post.created_at) }}, {{ formatDate(post.created_at) }}</span>
              <span class="meta-dot">·</span>
              <span>{{ post.comments?.length || 0 }} 评论</span>
            </div>
          </header>
          <div class="post-cover" v-if="post.cover_image">
            <img :src="post.cover_image" :alt="post.title" @error="onImgError" />
          </div>
          <div class="post-content" v-html="post.content"></div>
          <div class="post-comments" v-if="post.comments?.length">
            <h2>评论 ({{ post.comments.length }})</h2>
            <div class="comment-list">
              <div v-for="c in post.comments" :key="c.id" class="comment-item">
                <div class="comment-head">
                  <strong>{{ c.author_name }}</strong>
                  <span>{{ c.created_at?.slice(0, 10) }}</span>
                </div>
                <p>{{ c.content }}</p>
              </div>
            </div>
          </div>
        </article>
        <div class="back-nav">
          <router-link to="/">← 返回首页</router-link>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import ScrollGradient from '../components/ScrollGradient.vue'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import { fetchPostBySlug } from '../api.js'

const route = useRoute()
const post = ref(null)
const WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']

onMounted(async () => {
  try {
    post.value = await fetchPostBySlug(route.params.slug)
  } catch (e) { console.error(e) }
})

function formatDate(isoStr) {
  if (!isoStr) return ''
  const d = new Date(isoStr)
  return `${d.getMonth() + 1}月${d.getDate()}日, ${d.getFullYear()}`
}
function formatWeekday(isoStr) {
  if (!isoStr) return ''
  const d = new Date(isoStr)
  return WEEKDAYS[d.getDay()]
}
function onImgError(e) { e.target.src = 'data:image/svg+xml,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="400"><rect width="800" height="400" fill="#e8e5df"/></svg>') }
</script>

<style scoped>
.page-main { padding: 100px 0 60px; }
.container { max-width: 700px; margin: 0 auto; padding: 0 24px; }

.post-header { text-align: center; margin-bottom: 36px; }
.post-category {
  font-size: 12px; color: var(--color-accent); font-weight: 600;
  margin-bottom: 10px; font-family: 'JetBrains Mono', monospace;
}
.post-header h1 { font-size: 30px; font-weight: 800; line-height: 1.4; color: var(--color-text); margin: 0 0 12px; }
.post-meta { display: flex; justify-content: center; gap: 8px; font-size: 13px; color: var(--color-muted); flex-wrap: wrap; }
.meta-dot { opacity: 0.4; }

.post-cover { margin-bottom: 32px; border-radius: var(--radius-lg); overflow: hidden; }
.post-cover img { width: 100%; display: block; }

.post-content {
  font-size: 16px;
  line-height: 1.9;
  color: var(--color-text-secondary);
  word-break: break-word;
  overflow-wrap: break-word;
}
.post-content :deep(*) {
  max-width: 100%;
}
.post-content :deep(p) { margin-bottom: 18px; word-break: break-word; overflow-wrap: break-word; }
.post-content :deep(h2), .post-content :deep(h3) { margin: 36px 0 14px; color: var(--color-text); font-weight: 700; word-break: break-word; }
.post-content :deep(h2) { font-size: 22px; }
.post-content :deep(h3) { font-size: 18px; }
.post-content :deep(pre) { background: var(--color-code-bg); padding: 18px; border-radius: var(--radius-md); overflow-x: auto; margin-bottom: 18px; white-space: pre-wrap; word-break: break-word; }
.post-content :deep(code) { font-family: 'JetBrains Mono', monospace; font-size: 14px; word-break: break-word; }
.post-content :deep(img) { max-width: 100%; height: auto; display: block; border-radius: var(--radius-md); margin: 18px 0; }
.post-content :deep(figure) { max-width: 100%; margin: 18px 0; }
.post-content :deep(figure img) { margin: 0; }
.post-content :deep(figcaption) { font-size: 13px; color: var(--color-muted); text-align: center; margin-top: 8px; }
.post-content :deep(table) { width: 100%; border-collapse: collapse; margin-bottom: 18px; overflow-x: auto; display: block; }
.post-content :deep(th), .post-content :deep(td) { border: 1px solid var(--color-border); padding: 10px 14px; text-align: left; font-size: 14px; }
.post-content :deep(th) { background: var(--color-bg-secondary); font-weight: 600; }
.post-content :deep(blockquote) { border-left: 3px solid var(--color-accent); padding-left: 16px; margin: 18px 0; color: var(--color-muted); font-style: italic; word-break: break-word; }
.post-content :deep(ul), .post-content :deep(ol) { padding-left: 24px; margin-bottom: 18px; }
.post-content :deep(li) { margin-bottom: 6px; word-break: break-word; }
.post-content :deep(a) { color: var(--color-accent); border-bottom: 1px solid var(--color-accent-soft); word-break: break-word; }
.post-content :deep(a:hover) { border-bottom-color: var(--color-accent); }
.post-content :deep(hr) { border: none; border-top: 1px solid var(--color-border); margin: 32px 0; }
.post-content :deep(strong) { color: var(--color-text); font-weight: 600; }
.post-content :deep(em) { font-style: italic; }

.post-comments { margin-top: 48px; padding-top: 32px; border-top: 1px solid var(--color-border); }
.post-comments h2 { font-size: 18px; font-weight: 700; margin: 0 0 20px; color: var(--color-text); }
.comment-list { display: flex; flex-direction: column; gap: 0; }
.comment-item { padding: 16px 0; border-bottom: 1px solid var(--color-border); }
.comment-item:last-child { border-bottom: none; }
.comment-head { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 13px; }
.comment-head strong { color: var(--color-text); }
.comment-head span { color: var(--color-muted); font-size: 12px; }
.comment-item p { font-size: 14px; color: var(--color-text-secondary); line-height: 1.6; }

.back-nav { margin-top: 40px; text-align: center; }
.back-nav a { font-size: 14px; color: var(--color-muted); transition: color 0.2s; }
.back-nav a:hover { color: var(--color-accent); }
</style>
