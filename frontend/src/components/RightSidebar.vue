<script setup>
import { useSite } from '../composables/useSite'
import { formatDate } from '../utils/format'
import Icon from './Icon.vue'
const { latest, comments, stats, loading, error, load } = useSite()
</script>
<template>
  <aside class="right-sidebar" aria-label="博客动态">
    <section class="panel greeting-card">
      <span class="little-label">A MOMENT OF PEACE</span>
      <Icon name="coffee" :size="32" />
      <h2>歇一会儿吧</h2>
      <p>
        一杯咖啡，一段文字，
        <br />
        给忙碌的生活留一点空白。
      </p>
      <span class="greeting-dots">· · ·</span>
    </section>
    <section class="panel latest-widget">
      <h2 class="widget-title">
        <Icon name="clock" :size="18" />
        最近更新
      </h2>
      <p class="muted" v-if="loading && !latest.length">正在翻阅…</p>
      <p class="muted" v-else-if="error && !latest.length">
        加载失败
        <button class="text-button" @click="load">重试</button>
      </p>
      <p class="muted" v-else-if="!latest.length">新的故事正在酝酿。</p>
      <router-link
        v-for="post in latest"
        :key="post.id"
        :to="`/post/${post.slug}`"
        class="latest-item"
      >
        <time>{{ formatDate(post.created_at) }}</time>
        <span>{{ post.title }}</span>
      </router-link>
    </section>
    <section v-if="comments.length" class="panel comments-widget">
      <h2 class="widget-title">
        <Icon name="message" :size="18" />
        最近来信
      </h2>
      <router-link
        v-for="comment in comments.slice(0, 3)"
        :key="comment.id"
        :to="`/post/${comment.post_slug}#comments`"
        class="recent-comment"
      >
        <span class="comment-initial">
          {{ comment.author_name.slice(0, 1) }}
        </span>
        <div>
          <strong>{{ comment.author_name }}</strong>
          <p>{{ comment.content }}</p>
        </div>
      </router-link>
    </section>
    <section class="panel stats-widget">
      <h2 class="widget-title">
        <Icon name="leaf" :size="18" />
        小站足迹
      </h2>
      <div>
        <span>文章总数</span>
        <strong>{{ stats?.posts ?? '—' }} 篇</strong>
      </div>
      <div>
        <span>收到留言</span>
        <strong>{{ stats?.comments ?? '—' }} 条</strong>
      </div>
      <div>
        <span>最近更新</span>
        <strong>{{ formatDate(stats?.last_updated) }}</strong>
      </div>
      <a href="/feed/" class="rss-link">
        <Icon name="rss" :size="16" />
        订阅新的故事
        <Icon name="arrow" :size="15" />
      </a>
    </section>
  </aside>
</template>
