<script setup>
import { ref, computed, onMounted } from 'vue'
import { get } from '../api'
import { formatDate } from '../utils/format'
import Icon from '../components/Icon.vue'
const posts = ref([]),
  loading = ref(true),
  error = ref(false)
const groups = computed(() => {
  const result = new Map()
  for (const post of posts.value) {
    const year = new Date(post.created_at).getFullYear()
    if (!result.has(year)) result.set(year, [])
    result.get(year).push(post)
  }
  return [...result].map(([year, posts]) => ({ year, posts }))
})
async function load() {
  loading.value = true
  error.value = false
  try {
    posts.value = (await get('/api/archives/')).posts
  } catch {
    error.value = true
  } finally {
    loading.value = false
  }
}
onMounted(load)
</script>
<template>
  <header class="page-heading panel">
    <span class="eyebrow">
      <Icon name="archive" :size="16" />
      THE JOURNAL
    </span>
    <h1>
      时间留下的回声
      <span>.</span>
    </h1>
    <p>共 {{ posts.length }} 篇文字，一点一滴，都是来时的路。</p>
  </header>
  <section class="panel archive-panel">
    <div v-if="loading" class="empty-state" role="status">正在翻阅旧时光…</div>
    <div v-else-if="error" class="empty-state">
      <p>归档暂时加载失败。</p>
      <button class="primary-button" @click="load">重新加载</button>
    </div>
    <div v-else-if="!posts.length" class="empty-state">
      第一篇故事，即将开始。
    </div>
    <section
      v-for="group in groups"
      v-else
      :key="group.year"
      class="archive-year"
    >
      <h2>
        {{ group.year }}
        <small>{{ group.posts.length }} 篇</small>
      </h2>
      <router-link
        v-for="post in group.posts"
        :key="post.id"
        :to="`/post/${post.slug}`"
        class="archive-row"
      >
        <time>{{ formatDate(post.created_at).slice(5) }}</time>
        <span class="timeline-dot"></span>
        <strong>{{ post.title }}</strong>
        <small>{{ post.category__name || '未分类' }}</small>
        <Icon name="arrow" :size="16" />
      </router-link>
    </section>
  </section>
</template>
