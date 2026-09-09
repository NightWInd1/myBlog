<template>
  <div class="site-shell">
    <ScrollGradient />
    <Header />
    <main class="page-main">
      <div class="container">
        <div class="section-heading">
          <h1>搜索结果</h1>
          <p v-if="query">关键词：&quot;{{ query }}&quot; — 共 {{ total }} 条结果</p>
          <p v-else>请输入搜索关键词</p>
        </div>
        <div class="post-list" v-if="posts.length">
          <article v-for="(post, idx) in posts" :key="post.id" class="post-item">
            <span class="post-num">{{ pad(idx + 1) }}</span>
            <div class="post-body">
              <div class="post-main">
                <router-link :to="`/post/${post.slug}`" class="post-title-line">
                  <span class="post-category">// {{ post.category_name }}</span>
                  {{ post.title }}
                </router-link>
                <p class="post-excerpt" v-if="post.excerpt">{{ post.excerpt }}</p>
              </div>
              <div class="post-meta">
                <span class="post-weather">{{ getWeather(post) }}</span>
                <span class="post-date">{{ formatWeekday(post.created_at) }}, {{ formatDate(post.created_at) }}</span>
              </div>
            </div>
          </article>
        </div>
        <div class="empty" v-else-if="query && !loading">
          <p>未找到与 &quot;{{ query }}&quot; 相关的文章，试试其他关键词。</p>
        </div>
        <div class="pagination-wrap" v-if="pageCount > 1">
          <nav class="page-navigator">
            <button v-if="currentPage > 1" @click="go(currentPage - 1)" class="page-btn">上一页</button>
            <button
              v-for="p in pages"
              :key="p"
              :class="{ current: p === currentPage }"
              @click="go(p)"
              class="page-num"
            >{{ p }}</button>
            <button v-if="currentPage < pageCount" @click="go(currentPage + 1)" class="page-btn">下一页</button>
          </nav>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import ScrollGradient from '../components/ScrollGradient.vue'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import { searchPosts } from '../api.js'

const route = useRoute()
const posts = ref([])
const total = ref(0)
const currentPage = ref(1)
const pageCount = ref(1)
const loading = ref(false)
const query = computed(() => route.query.q || '')

const WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
const WEATHER_EMOJI = ['☀️','⛅','☁️','🌧️','⛈️','🌤️','🌦️','🌈','❄️','🌬️']

const pages = computed(() => {
  const arr = []
  for (let i = 1; i <= pageCount.value; i++) arr.push(i)
  return arr
})

async function doSearch(page = 1) {
  if (!query.value) { posts.value = []; total.value = 0; return }
  loading.value = true
  try {
    const data = await searchPosts(query.value, page)
    posts.value = data.results
    total.value = data.count
    currentPage.value = page
    pageCount.value = Math.ceil(data.count / 10)
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}

function go(p) {
  currentPage.value = p
  doSearch(p)
}

onMounted(() => doSearch())
watch(query, () => doSearch())

function pad(n) { return String(n).padStart(2, '0') }
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
function getWeather(post) {
  if (!post.id) return '☀️'
  return WEATHER_EMOJI[post.id % WEATHER_EMOJI.length]
}
</script>

<style scoped>
.page-main { padding: 100px 0 60px; }
.container { max-width: 700px; margin: 0 auto; padding: 0 24px; }
.section-heading { margin-bottom: 36px; text-align: center; }
.section-heading h1 { font-size: 28px; font-weight: 800; margin: 0 0 8px; color: var(--color-text); }
.section-heading p { color: var(--color-muted); font-size: 14px; }

.post-list { display: flex; flex-direction: column; }
.post-item { display: flex; align-items: flex-start; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--color-border); transition: border-color 0.2s; }
.post-item:last-child { border-bottom: none; }
.post-item:hover { border-color: var(--color-accent); }

.post-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px; color: var(--color-muted);
  min-width: 28px; flex-shrink: 0; padding-top: 1px;
}

.post-body { flex: 1; display: flex; justify-content: space-between; gap: 20px; min-width: 0; }
.post-main { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px; }
.post-title-line { font-size: 15px; font-weight: 500; color: var(--color-text); transition: color 0.2s; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.post-title-line:hover { color: var(--color-accent); }
.post-category { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: var(--color-accent); font-weight: 400; margin-right: 6px; }
.post-excerpt { font-size: 13px; color: var(--color-muted); line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.post-meta { display: flex; flex-direction: column; align-items: flex-end; gap: 3px; flex-shrink: 0; }
.post-date { font-size: 12px; color: var(--color-muted); white-space: nowrap; }
.post-weather { font-size: 14px; line-height: 1; }

.empty { text-align: center; padding: 60px 0; color: var(--color-muted); font-size: 15px; }

.pagination-wrap { margin-top: 28px; display: flex; justify-content: center; }
.page-navigator { display: flex; align-items: center; gap: 4px; }
.page-btn { padding: 6px 14px; border-radius: var(--radius-sm); font-size: 13px; color: var(--color-muted); transition: all 0.2s; }
.page-btn:hover { color: var(--color-text); background: var(--color-bg-hover); }
.page-num {
  min-width: 34px; height: 34px; display: flex; align-items: center; justify-content: center;
  border-radius: var(--radius-sm); font-size: 14px; font-weight: 500; color: var(--color-muted); transition: all 0.2s;
}
.page-num:hover { color: var(--color-text); background: var(--color-bg-hover); }
.page-num.current { background: var(--color-accent); color: #fff; }

@media (max-width: 768px) {
  .post-body { flex-direction: column; gap: 6px; }
  .post-title-line { white-space: normal; }
  .post-meta { flex-direction: row; align-items: center; gap: 8px; }
}
</style>
