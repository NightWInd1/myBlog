<script setup>
import { ref, watch, nextTick, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import DOMPurify from 'dompurify'
import { fetchPostBySlug } from '../api'
import { formatDate } from '../utils/format'
import { site } from '../config/site'
import Icon from '../components/Icon.vue'
const route = useRoute()
const post = ref(null),
  loading = ref(true),
  error = ref(''),
  headings = ref([]),
  body = ref('')
const coverFailed = ref(false)
const tocOpen = ref(true)
let controller
function prepareContent(html) {
  const document = new DOMParser().parseFromString(
    DOMPurify.sanitize(html),
    'text/html',
  )
  const outline = []
  document.querySelectorAll('h2, h3').forEach((heading, index) => {
    heading.id = `section-${index + 1}`
    outline.push({
      id: heading.id,
      title: heading.textContent,
      level: heading.tagName,
    })
  })
  document.querySelectorAll('a[target="_blank"]').forEach((link) => {
    link.rel = 'noopener noreferrer'
  })
  document.querySelectorAll('img').forEach((img) => {
    img.loading = 'lazy'
    img.decoding = 'async'
  })
  headings.value = outline
  body.value = document.body.innerHTML
}
async function load() {
  controller?.abort()
  const current = new AbortController()
  controller = current
  loading.value = true
  post.value = null
  coverFailed.value = false
  error.value = ''
  headings.value = []
  body.value = ''
  try {
    const data = await fetchPostBySlug(route.params.slug, {
      signal: current.signal,
    })
    post.value = data
    document.title = `${data.title} · 晚风如歌`
    prepareContent(data.content)
  } catch (e) {
    if (e.name !== 'AbortError') error.value = e.message
  } finally {
    if (current === controller) {
      loading.value = false
      await nextTick()
      if (route.hash)
        document
          .getElementById(decodeURIComponent(route.hash.slice(1)))
          ?.scrollIntoView()
    }
  }
}
watch(() => route.params.slug, load, { immediate: true })
onUnmounted(() => controller?.abort())
</script>
<template>
  <div v-if="loading" class="panel empty-state" aria-busy="true">
    <Icon name="book" :size="32" />
    <p>正在打开这段故事…</p>
  </div>
  <div v-else-if="error" class="panel empty-state" role="alert">
    <Icon name="info" :size="34" />
    <h1>{{ error }}</h1>
    <button class="primary-button" @click="load">重新加载</button>
    <router-link to="/" class="subtle-link">返回首页</router-link>
  </div>
  <template v-else-if="post">
    <nav class="breadcrumbs" aria-label="面包屑">
      <router-link to="/">首页</router-link>
      <Icon name="chevron" :size="13" />
      <router-link
        v-if="post.category_slug"
        :to="`/category/${post.category_slug}`"
      >
        {{ post.category_name }}
      </router-link>
      <span v-else>文章</span>
      <Icon name="chevron" :size="13" />
      <span>正文</span>
    </nav>
    <article class="panel article-panel">
      <header class="article-header">
        <span class="eyebrow">
          <Icon name="book" :size="15" />
          {{ post.category_name }}
        </span>
        <h1>{{ post.title }}</h1>
        <div class="post-meta">
          <span>{{ post.author_name }}</span>
          <time>
            <Icon name="calendar" :size="14" />
            {{ formatDate(post.created_at) }}
          </time>
          <span>
            <Icon name="clock" :size="14" />
            {{ post.reading_minutes }} 分钟阅读
          </span>
        </div>
      </header>
      <img
        v-if="post.cover_image && !coverFailed"
        :src="post.cover_image"
        :alt="post.title"
        class="article-cover"
        @error="coverFailed = true"
      />
      <img
        v-else
        class="article-cover"
        :src="site.postImages?.[0] || site.heroImage"
        :alt="post.title"
      />
      <nav v-if="headings.length" class="article-toc" aria-label="文章目录">
        <button @click="tocOpen = !tocOpen" :aria-expanded="tocOpen">
          <span>
            <Icon name="list" :size="17" />
            本文目录
          </span>
          <Icon :name="tocOpen ? 'up' : 'down'" :size="17" />
        </button>
        <ol v-if="tocOpen">
          <li
            v-for="heading in headings"
            :key="heading.id"
            :class="{ nested: heading.level === 'H3' }"
          >
            <a :href="`#${heading.id}`">{{ heading.title }}</a>
          </li>
        </ol>
      </nav>
      <div class="article-prose" v-html="body"></div>
      <footer class="article-signoff">
        <Icon name="leaf" :size="22" />
        <p>
          感谢你读到这里。
          <br />
          <span>愿我们始终保持好奇，继续热爱。</span>
        </p>
        <small>最后更新于 {{ formatDate(post.updated_at) }}</small>
      </footer>
      <section id="comments" class="article-comments">
        <h2>
          <Icon name="message" :size="20" />
          留下的回声
          <span>{{ post.comments.length }}</span>
        </h2>
        <div v-if="!post.comments.length" class="comment-empty">
          这里还没有留言，感谢你的阅读。
        </div>
        <div
          v-for="comment in post.comments"
          :key="comment.id"
          class="article-comment"
        >
          <span class="comment-initial">
            {{ comment.author_name.slice(0, 1) }}
          </span>
          <div>
            <div class="comment-heading">
              <strong>{{ comment.author_name }}</strong>
              <time>{{ formatDate(comment.created_at) }}</time>
            </div>
            <p>{{ comment.content }}</p>
          </div>
        </div>
      </section>
    </article>
    <router-link class="back-home" to="/">← 回到首页，继续探索</router-link>
  </template>
</template>
