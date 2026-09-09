<template>
  <div class="site-shell">
    <ScrollGradient />
    <Header />
    <main class="page-main">
      <div class="container">
        <div class="section-heading">
          <span class="section-tag">{{ categoryInfo.tag }}</span>
          <h1>{{ categoryInfo.name }}</h1>
          <p>{{ categoryInfo.desc }}</p>
        </div>
        <div class="post-list" v-if="posts.length">
          <article v-for="(post, idx) in posts" :key="post.id" class="post-item">
            <span class="post-num">{{ pad(idx + 1) }}</span>
            <div class="post-body">
              <div class="post-main">
                <router-link :to="`/post/${post.slug}`" class="post-title-line">
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
        <div class="empty" v-else-if="!loading">
          <p>该分类下暂无文章，敬请期待。</p>
          <router-link to="/" class="back-link">← 返回首页</router-link>
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
import { fetchPosts, get } from '../api.js'

const route = useRoute()
const posts = ref([])
const loading = ref(false)
const slug = computed(() => route.params.slug)
const categoryMeta = ref({ name: '', tag: 'CAT', desc: '文章分类' })

const DEFAULT_META = {
  tech: { name: '技术文章', tag: 'TECH', desc: '记录学习与工作中的技术实践' },
  life: { name: '生活随笔', tag: 'LIFE', desc: '记录生活中的点点滴滴' },
}

const categoryInfo = computed(() => categoryMeta.value)

const TAG_WORDS = {
  posts: 'POSTS', memories: 'MEMORY', poetry: 'POETRY',
  changes: 'NEWS', more: 'MORE',
}

async function loadCategoryMeta() {
  try {
    const tree = await get('/api/categories/')
    for (const parent of tree) {
      if (parent.slug === slug.value) {
        categoryMeta.value = { name: parent.name, tag: TAG_WORDS[parent.slug] || 'CAT', desc: parent.description || '文章分类' }
        return
      }
      for (const child of parent.children) {
        if (child.slug === slug.value) {
          categoryMeta.value = { name: child.name, tag: TAG_WORDS[parent.slug] || 'CAT', desc: child.description || parent.name }
          return
        }
      }
    }
    categoryMeta.value = DEFAULT_META[slug.value] || { name: slug.value, tag: 'CAT', desc: '文章分类' }
  } catch {
    categoryMeta.value = DEFAULT_META[slug.value] || { name: slug.value, tag: 'CAT', desc: '文章分类' }
  }
}

async function loadPosts() {
  loading.value = true
  try {
    const data = await fetchPosts(1, { category: slug.value })
    posts.value = data.results
  } catch (e) {
    console.error(e)
  } finally {
    loading.value = false
  }
}

const WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
const WEATHER_EMOJI = ['☀️','⛅','☁️','🌧️','⛈️','🌤️','🌦️','🌈','❄️','🌬️']

async function loadPage() {
  await loadCategoryMeta()
  await loadPosts()
}

onMounted(() => loadPage())
watch(slug, () => loadPage())

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
.section-tag {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--color-accent);
  background: var(--color-accent-soft);
  padding: 3px 10px;
  border-radius: var(--radius-sm);
}
.section-heading h1 { font-size: 30px; font-weight: 800; margin: 10px 0 6px; color: var(--color-text); }
.section-heading p { font-size: 14px; color: var(--color-muted); }

.post-list { display: flex; flex-direction: column; }
.post-item { display: flex; align-items: flex-start; gap: 16px; padding: 16px 0; border-bottom: 1px solid var(--color-border); transition: border-color 0.2s; }
.post-item:last-child { border-bottom: none; }
.post-item:hover { border-color: var(--color-accent); }

.post-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px; color: var(--color-muted);
  min-width: 28px; flex-shrink: 0; padding-top: 2px;
}

.post-body { flex: 1; display: flex; justify-content: space-between; gap: 20px; min-width: 0; }
.post-main { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px; }
.post-title-line { font-size: 15px; font-weight: 500; color: var(--color-text); transition: color 0.2s; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.post-title-line:hover { color: var(--color-accent); }
.post-excerpt { font-size: 13px; color: var(--color-muted); line-height: 1.5; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.post-meta { display: flex; flex-direction: column; align-items: flex-end; gap: 3px; flex-shrink: 0; }
.post-date { font-size: 12px; color: var(--color-muted); white-space: nowrap; }
.post-weather { font-size: 14px; line-height: 1; }

.empty { text-align: center; padding: 60px 0; color: var(--color-muted); font-size: 15px; }
.back-link { display: inline-block; margin-top: 16px; color: var(--color-accent); font-size: 14px; transition: opacity 0.2s; }
.back-link:hover { opacity: 0.8; }

@media (max-width: 768px) {
  .post-body { flex-direction: column; gap: 6px; }
  .post-title-line { white-space: normal; }
  .post-meta { flex-direction: row; align-items: center; gap: 8px; }
}
</style>
