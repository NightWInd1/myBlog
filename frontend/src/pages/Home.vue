<template>
  <div class="site-shell">
    <ScrollGradient />
    <Header />
    <main>
      <Hero :stats="siteStats" />
      <section class="home-content">
        <div class="home-grid">
          <div class="home-left">
            <h2 class="section-title">近期笔墨</h2>
            <div class="post-list">
              <article v-for="(post, idx) in posts" :key="post.id" class="post-item">
                <span class="post-num">{{ pad(idx + 1) }}</span>
                <div class="post-body">
                  <div class="post-main">
                    <router-link :to="`/post/${post.slug}`" class="post-title">
                      <span class="post-category">// {{ post.category_name || '未分类' }}</span>
                      {{ post.title }}
                    </router-link>
                    <p class="post-excerpt" v-if="post.excerpt">{{ post.excerpt }}</p>
                  </div>
                  <div class="post-meta">
                    <span class="post-weather" :title="getWeatherDesc(post)">{{ getWeather(post) }}</span>
                    <span class="post-date">{{ formatWeekday(post.created_at) }}, {{ formatDate(post.created_at) }}</span>
                  </div>
                </div>
              </article>
            </div>
            <div class="pagination-wrap" v-if="pageCount > 1">
              <nav class="page-navigator">
                <button v-if="currentPage > 1" @click="fetchPage(currentPage - 1)" class="page-btn">上一页</button>
                <button v-for="p in pages" :key="p" :class="{ current: p === currentPage }" @click="fetchPage(p)" class="page-num">{{ p }}</button>
                <button v-if="currentPage < pageCount" @click="fetchPage(currentPage + 1)" class="page-btn">下一页</button>
              </nav>
            </div>
          </div>

          <aside class="home-right">
            <div class="side-box">
              <h3 class="side-title">杂言</h3>
              <p class="side-desc">静水流深，闻喧享静。记录日常的点滴思考与灵感碎片。</p>
            </div>

            <div class="side-box" v-if="comments.length">
              <h3 class="side-title">来信</h3>
              <div class="side-comments">
                <div v-for="c in comments" :key="c.id" class="sc-item">
                  <div class="sc-head">
                    <span class="sc-author">{{ c.author_name }}</span>
                    <span class="sc-time">{{ c.created_at?.slice(0, 10) }}</span>
                  </div>
                  <p class="sc-content">{{ c.content }}</p>
                </div>
              </div>
            </div>

            <div class="side-box side-subscribe">
              <p class="subscribe-desc">♥ Subscribe</p>
              <p class="subscribe-hint">订阅博客，不错过任何更新。</p>
              <a href="/feed/" class="subscribe-btn">RSS 订阅</a>
            </div>
          </aside>
        </div>
      </section>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import ScrollGradient from '../components/ScrollGradient.vue'
import Header from '../components/Header.vue'
import Hero from '../components/Hero.vue'
import Footer from '../components/Footer.vue'
import { fetchPosts, fetchLatestComments } from '../api.js'

const posts = ref([])
const comments = ref([])
const currentPage = ref(1)
const pageCount = ref(1)
const totalCount = ref(0)
const commentCount = ref(0)

const WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
const WEATHER_EMOJI = ['☀️','⛅','☁️','🌧️','⛈️','🌤️','🌦️','🌈','❄️','🌬️','🌫️','🌨️','🌩️','🌪️','💨']
const WEATHER_DESC = ['晴','多云','阴','小雨','雷雨','晴间多云','阵雨','彩虹','雪','大风','雾','大雪','暴雨','台风','微风']

const siteStats = computed(() => ({
  posts: totalCount.value,
  categories: 3,
  comments: commentCount.value,
}))

const pages = computed(() => {
  const arr = []
  for (let i = 1; i <= pageCount.value; i++) arr.push(i)
  return arr
})

async function fetchPage(page) {
  currentPage.value = page
  const data = await fetchPosts(page)
  posts.value = data.results
  pageCount.value = Math.ceil(data.count / 10)
  totalCount.value = data.count
}

onMounted(async () => {
  try {
    const [postData, commentData] = await Promise.all([
      fetchPosts(1),
      fetchLatestComments(),
    ])
    posts.value = postData.results
    pageCount.value = Math.ceil(postData.count / 10)
    totalCount.value = postData.count
    comments.value = commentData
    commentCount.value = commentData.length
  } catch (e) {
    console.error('Failed to fetch data:', e)
  }
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
function getWeatherDesc(post) {
  if (!post.id) return '晴'
  return WEATHER_DESC[post.id % WEATHER_DESC.length]
}
</script>

<style scoped>
.home-content {
  max-width: 1060px;
  margin: 0 auto;
  padding: 0 24px 60px;
}
.home-grid {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 48px;
  align-items: start;
}

.home-left {
  min-width: 0;
}
.section-title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--color-text);
  padding-bottom: 12px;
  border-bottom: 1px solid var(--color-border);
}

.post-list { display: flex; flex-direction: column; }
.post-item {
  display: flex; align-items: flex-start; gap: 16px;
  padding: 16px 0;
  border-bottom: 1px solid var(--color-border);
  transition: border-color 0.2s;
}
.post-item:last-child { border-bottom: none; }
.post-item:hover { border-color: var(--color-accent); }

.post-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px; color: var(--color-muted);
  min-width: 28px; flex-shrink: 0; padding-top: 2px;
}

.post-body { flex: 1; display: flex; justify-content: space-between; gap: 20px; min-width: 0; }
.post-main { flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px; }
.post-title {
  font-size: 15px; font-weight: 500;
  color: var(--color-text); transition: color 0.2s;
  overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.post-title:hover { color: var(--color-accent); }
.post-category {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px; color: var(--color-accent); font-weight: 400;
  margin-right: 6px;
}
.post-excerpt {
  font-size: 13px; color: var(--color-muted); line-height: 1.5;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}
.post-meta { display: flex; flex-direction: column; align-items: flex-end; gap: 3px; flex-shrink: 0; }
.post-date { font-size: 12px; color: var(--color-muted); white-space: nowrap; }
.post-weather { font-size: 14px; line-height: 1; }

.pagination-wrap { margin-top: 28px; display: flex; justify-content: center; }
.page-navigator { display: flex; align-items: center; gap: 4px; }
.page-btn {
  padding: 6px 14px; border-radius: var(--radius-sm);
  font-size: 13px; color: var(--color-muted); transition: all 0.2s;
}
.page-btn:hover { color: var(--color-text); background: var(--color-bg-hover); }
.page-num {
  min-width: 34px; height: 34px;
  display: flex; align-items: center; justify-content: center;
  border-radius: var(--radius-sm);
  font-size: 14px; font-weight: 500; color: var(--color-muted);
  transition: all 0.2s;
}
.page-num:hover { color: var(--color-text); background: var(--color-bg-hover); }
.page-num.current { background: var(--color-accent); color: #fff; }

.home-right {
  position: sticky;
  top: 80px;
  display: flex; flex-direction: column; gap: 20px;
}
.side-box {
  background: rgba(128, 128, 128, 0.04);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-md);
  padding: 18px;
}
.side-title {
  font-size: 14px; font-weight: 600;
  color: var(--color-text); margin-bottom: 10px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--color-border);
}
.side-desc {
  font-size: 13px; color: var(--color-muted); line-height: 1.6;
}

.side-comments { display: flex; flex-direction: column; gap: 0; }
.sc-item { padding: 10px 0; border-bottom: 1px solid var(--color-border); }
.sc-item:last-child { border-bottom: none; padding-bottom: 0; }
.sc-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px; }
.sc-author { font-size: 13px; font-weight: 600; color: var(--color-text); }
.sc-time { font-size: 11px; color: var(--color-muted); }
.sc-content { font-size: 12px; color: var(--color-text-secondary); line-height: 1.5; }

.side-subscribe {
  text-align: center;
  background: transparent;
  border-style: dashed;
}
.subscribe-desc { font-size: 15px; font-weight: 600; color: var(--color-accent); margin-bottom: 4px; }
.subscribe-hint { font-size: 12px; color: var(--color-muted); margin-bottom: 12px; }
.subscribe-btn {
  display: inline-flex; align-items: center; justify-content: center;
  padding: 7px 20px; border-radius: var(--radius-sm);
  background: var(--color-accent); color: #fff;
  font-size: 13px; font-weight: 500; transition: background 0.2s;
}
.subscribe-btn:hover { background: var(--color-accent-hover); }

@media (max-width: 900px) {
  .home-grid { grid-template-columns: 1fr; gap: 32px; }
  .home-right { position: static; }
}
@media (max-width: 768px) {
  .post-body { flex-direction: column; gap: 6px; }
  .post-title { white-space: normal; }
  .post-meta { flex-direction: row; align-items: center; gap: 8px; }
}
</style>
