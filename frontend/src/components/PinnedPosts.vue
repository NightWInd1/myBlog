<template>
  <section class="sticky-section" v-if="posts.length">
    <div class="container">
      <div class="section-heading section-heading--row">
        <div>
          <span class="section-tag">PINNED</span>
          <h2>置顶推荐</h2>
        </div>
        <p>{{ posts.length }} 篇精选文章</p>
      </div>
      <div class="sticky-grid" :class="`sticky-grid--${posts.length}`">
        <router-link v-for="post in posts" :key="post.id" class="sticky-card" :to="`/post/${post.slug}`">
          <div class="sticky-card-media">
            <img :src="post.cover_image || `https://picsum.photos/seed/${post.id}/600/400`" :alt="post.title" loading="lazy" @error="onImgError" />
          </div>
          <div class="sticky-card-overlay"></div>
          <div class="sticky-card-body">
            <span class="sticky-card-badge">// {{ post.category_name?.toUpperCase() || 'PINNED' }}</span>
            <h3>{{ post.title }}</h3>
            <p>{{ post.excerpt }}</p>
            <span class="sticky-card-date">{{ post.created_at?.slice(0, 10) }}</span>
          </div>
        </router-link>
      </div>
    </div>
  </section>
</template>

<script setup>
defineProps({ posts: { type: Array, default: () => [] } })
function onImgError(e) { e.target.src = 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="600" height="400" fill="%232d3748"><rect width="600" height="400"/></svg>' }
</script>

<style scoped>
.sticky-section { padding: 60px 0; position: relative; z-index: 1; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
.section-heading { margin-bottom: 32px; }
.section-heading--row { display: flex; justify-content: space-between; align-items: flex-end; }
.section-heading h2 { font-size: 24px; font-weight: 700; margin: 8px 0 0; color: var(--color-text); }
.section-heading p { color: var(--color-muted); font-size: 14px; margin: 0; }
.section-tag { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #4299e1; background: rgba(66, 153, 225, .12); padding: 2px 8px; border-radius: 4px; }
.sticky-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; }
.sticky-grid--2 { grid-template-columns: repeat(2, 1fr); }
.sticky-grid--1 { grid-template-columns: 1fr; }
.sticky-card { position: relative; border-radius: 12px; overflow: hidden; height: 340px; display: block; text-decoration: none; color: #fff; }
.sticky-card-media { position: absolute; inset: 0; }
.sticky-card-media img { width: 100%; height: 100%; object-fit: cover; transition: transform .4s; }
.sticky-card:hover .sticky-card-media img { transform: scale(1.05); }
.sticky-card-overlay { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(0,0,0,.8) 0%, rgba(0,0,0,.25) 50%, rgba(0,0,0,.1) 100%); }
.sticky-card-body { position: absolute; bottom: 0; left: 0; right: 0; padding: 24px; z-index: 2; }
.sticky-card-badge { font-family: 'JetBrains Mono', monospace; font-size: 10px; background: rgba(66, 153, 225, .3); padding: 2px 8px; border-radius: 4px; }
.sticky-card-body h3 { font-size: 16px; font-weight: 700; margin: 8px 0; line-height: 1.4; }
.sticky-card-body p { font-size: 12px; line-height: 1.5; opacity: .8; margin: 0 0 8px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
.sticky-card-date { font-size: 12px; opacity: .6; }

@media (max-width: 768px) {
  .sticky-grid, .sticky-grid--2, .sticky-grid--1 { grid-template-columns: 1fr; }
  .sticky-card { height: 260px; }
}
</style>
