<template>
  <section class="stream-section" id="post-stream">
    <div class="stream-inner">
      <h2 class="section-title">最新文章</h2>

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
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  posts: { type: Array, default: () => [] },
  currentPage: { type: Number, default: 1 },
  pageCount: { type: Number, default: 1 },
})

const emit = defineEmits(['page-change'])

const pages = computed(() => {
  const arr = []
  for (let i = 1; i <= props.pageCount; i++) arr.push(i)
  return arr
})

const WEEKDAYS = ['周日', '周一', '周二', '周三', '周四', '周五', '周六']
const WEATHER_EMOJI = ['☀️','⛅','☁️','🌧️','⛈️','🌤️','🌦️','🌈','❄️','🌬️','🌫️','🌨️','🌩️','🌪️','💨']
const WEATHER_DESC = ['晴','多云','阴','小雨','雷雨','晴间多云','阵雨','彩虹','雪','大风','雾','大雪','暴雨','台风','微风']

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
  const idx = post.id % WEATHER_EMOJI.length
  return WEATHER_EMOJI[idx]
}

function getWeatherDesc(post) {
  if (!post.id) return '晴'
  const idx = post.id % WEATHER_DESC.length
  return WEATHER_DESC[idx]
}

function go(p) { emit('page-change', p) }
</script>

<style scoped>
.stream-section {
  padding: 0 0 60px;
}
.stream-inner {
  max-width: 700px;
  margin: 0 auto;
  padding: 0 24px;
}
.section-title {
  font-size: 18px;
  font-weight: 700;
  margin-bottom: 20px;
  color: var(--color-text);
  padding-bottom: 12px;
  border-bottom: 1px solid var(--color-border);
}

.post-list {
  display: flex;
  flex-direction: column;
}
.post-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  padding: 16px 0;
  border-bottom: 1px solid var(--color-border);
  transition: border-color 0.2s;
}
.post-item:last-child { border-bottom: none; }
.post-item:hover { border-color: var(--color-accent); }

.post-num {
  font-family: 'JetBrains Mono', monospace;
  font-size: 13px;
  color: var(--color-muted);
  min-width: 28px;
  flex-shrink: 0;
  padding-top: 2px;
}

.post-body {
  flex: 1;
  display: flex;
  justify-content: space-between;
  gap: 20px;
  min-width: 0;
}
.post-main {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.post-title {
  font-size: 15px;
  font-weight: 500;
  color: var(--color-text);
  transition: color 0.2s;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.post-title:hover { color: var(--color-accent); }

.post-category {
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--color-accent);
  font-weight: 400;
  margin-right: 6px;
}

.post-excerpt {
  font-size: 13px;
  color: var(--color-muted);
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.post-meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 3px;
  flex-shrink: 0;
}
.post-date {
  font-size: 12px;
  color: var(--color-muted);
  white-space: nowrap;
}
.post-weather {
  font-size: 14px;
  line-height: 1;
}

.pagination-wrap {
  margin-top: 28px;
  display: flex;
  justify-content: center;
}
.page-navigator {
  display: flex;
  align-items: center;
  gap: 4px;
}
.page-btn {
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  font-size: 13px;
  color: var(--color-muted);
  transition: all 0.2s;
}
.page-btn:hover {
  color: var(--color-text);
  background: var(--color-bg-hover);
}
.page-num {
  min-width: 34px; height: 34px;
  display: flex; align-items: center; justify-content: center;
  border-radius: var(--radius-sm);
  font-size: 14px; font-weight: 500;
  color: var(--color-muted);
  transition: all 0.2s;
}
.page-num:hover {
  color: var(--color-text);
  background: var(--color-bg-hover);
}
.page-num.current {
  background: var(--color-accent);
  color: #fff;
}

@media (max-width: 768px) {
  .post-body { flex-direction: column; gap: 6px; }
  .post-title { white-space: normal; }
  .post-meta { flex-direction: row; align-items: center; gap: 8px; }
}
</style>
