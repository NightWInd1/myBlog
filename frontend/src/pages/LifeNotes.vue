<template>
  <div class="site-shell">
    <ScrollGradient />
    <Header />
    <main class="page-main">
      <div class="container">
        <div class="section-heading">
          <span class="section-tag">LIFE</span>
          <h1>生活随笔</h1>
          <p>记录生活中的点点滴滴</p>
        </div>
        <div class="post-list">
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
        <div class="empty" v-if="!posts.length">
          <p>暂无文章</p>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import ScrollGradient from '../components/ScrollGradient.vue'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import { fetchPosts } from '../api.js'

const posts = ref([])
const WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
const WEATHER_EMOJI = ['☀️','⛅','☁️','🌧️','⛈️','🌤️','🌦️','🌈','❄️','🌬️']

onMounted(async () => {
  try {
    const data = await fetchPosts(1, { category: 'life' })
    posts.value = data.results
  } catch (e) { console.error(e) }
})

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
  min-width: 28px; flex-shrink: 0; padding-top: 1px;
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

@media (max-width: 768px) {
  .post-body { flex-direction: column; gap: 6px; }
  .post-title-line { white-space: normal; }
  .post-meta { flex-direction: row; align-items: center; gap: 8px; }
}
</style>
