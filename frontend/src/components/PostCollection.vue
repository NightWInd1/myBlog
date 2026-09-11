<script setup>
import { computed, ref, watch, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { fetchPosts, searchPosts } from '../api'
import { useAppearance } from '../composables/useAppearance'
import PostCard from './PostCard.vue'
import Pagination from './Pagination.vue'
import Icon from './Icon.vue'
const props = defineProps({
  category: { type: String, default: '' },
  query: { type: String, default: '' },
  search: Boolean,
})
const route = useRoute(),
  router = useRouter()
const { layout } = useAppearance()
const posts = ref([]),
  count = ref(0),
  loading = ref(true),
  error = ref('')
const sort = ref('pinned')
const page = computed(() =>
  Math.max(1, Math.floor(Number(route.query.page) || 1)),
)
let controller
async function load() {
  controller?.abort()
  const current = new AbortController()
  controller = current
  error.value = ''
  loading.value = true
  try {
    const data = props.search
      ? await searchPosts(props.query, page.value, { signal: current.signal })
      : await fetchPosts(
          page.value,
          {
            ...(props.category ? { category: props.category } : {}),
            ordering: sort.value,
          },
          { signal: current.signal },
        )
    posts.value = data.results
    count.value = data.count
  } catch (e) {
    if (e.name !== 'AbortError') {
      error.value = e.message
      posts.value = []
    }
  } finally {
    if (controller === current) loading.value = false
  }
}
function go(value) {
  router.push({
    query: { ...route.query, page: value > 1 ? value : undefined },
    hash: '#main-content',
  })
}
function sortChanged() {
  if (page.value > 1) go(1)
  else load()
}
watch([() => props.category, () => props.query, page], load, {
  immediate: true,
})
onUnmounted(() => controller?.abort())
</script>
<template>
  <div class="collection-toolbar">
    <div>
      <Icon :name="search ? 'search' : 'book'" :size="18" />
      <h2>{{ search ? '搜索结果' : '最近的文字' }}</h2>
      <span class="count-badge" v-if="!loading && !error">{{ count }}</span>
    </div>
    <div class="collection-actions">
      <select
        v-if="!search"
        v-model="sort"
        @change="sortChanged"
        aria-label="文章排序"
      >
        <option value="pinned">置顶优先</option>
        <option value="latest">最新发布</option>
      </select>
      <span class="toolbar-divider"></span>
      <button
        :class="{ selected: layout === 'list' }"
        @click="layout = 'list'"
        aria-label="列表布局"
        :aria-pressed="layout === 'list'"
      >
        <Icon name="list" :size="18" />
      </button>
      <button
        :class="{ selected: layout === 'grid' }"
        @click="layout = 'grid'"
        aria-label="网格布局"
        :aria-pressed="layout === 'grid'"
      >
        <Icon name="grid" :size="16" />
      </button>
    </div>
  </div>
  <div
    v-if="loading"
    class="post-skeletons"
    aria-busy="true"
    aria-label="正在加载文章"
  >
    <div v-for="n in 3" :key="n" class="panel skeleton-card">
      <i></i>
      <i></i>
      <i></i>
    </div>
  </div>
  <div v-else-if="error" class="panel empty-state" role="alert">
    <Icon name="info" :size="34" />
    <h2>暂时没有连上小站</h2>
    <p>{{ error }}</p>
    <button class="primary-button" @click="load">重新加载</button>
  </div>
  <div v-else-if="!posts.length" class="panel empty-state">
    <Icon :name="search ? 'search' : 'leaf'" :size="36" />
    <h2>{{ search ? '还没有找到这段文字' : '故事，还在慢慢生长' }}</h2>
    <p>
      {{
        search
          ? '试试更简短的关键词，或换一个说法。'
          : '这里暂时没有文章，去看看其他分类吧。'
      }}
    </p>
    <router-link to="/" class="primary-button">
      回到首页
      <Icon name="arrow" :size="16" />
    </router-link>
  </div>
  <template v-else>
    <div class="post-collection" :class="{ 'grid-view': layout === 'grid' }">
      <PostCard
        v-for="(post, index) in posts"
        :key="post.id"
        :post="post"
        :index="index"
      />
    </div>
    <Pagination
      :page="page"
      :total-pages="Math.ceil(count / 10)"
      @change="go"
    />
    <p class="collection-end" v-if="count <= 10">
      <span></span>
      <Icon name="leaf" :size="15" />
      每一次记录，都算数
      <span></span>
    </p>
  </template>
</template>
