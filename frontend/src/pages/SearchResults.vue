<script setup>
import { ref, watch, computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import PostCollection from '../components/PostCollection.vue'
import Icon from '../components/Icon.vue'
const route = useRoute(),
  router = useRouter()
const query = computed(() => String(route.query.q || '').trim())
const input = ref(query.value)
watch(query, (value) => {
  input.value = value
})
function search() {
  router.push({
    path: '/search',
    query: input.value.trim() ? { q: input.value.trim() } : {},
  })
}
</script>
<template>
  <header class="page-heading panel">
    <span class="eyebrow">
      <Icon name="search" :size="16" />
      SEARCH
    </span>
    <h1>找找你感兴趣的</h1>
    <p>也许，你正在寻找的灵感就在这里。</p>
    <form class="page-search" @submit.prevent="search">
      <input
        v-model="input"
        placeholder="输入关键词…"
        aria-label="搜索关键词"
      />
      <button type="submit" class="primary-button">
        搜索
        <Icon name="search" :size="16" />
      </button>
    </form>
  </header>
  <PostCollection v-if="query" search :query="query" />
  <div v-else class="panel empty-state">
    <Icon name="search" :size="36" />
    <p>输入关键词，开始探索。</p>
  </div>
</template>
