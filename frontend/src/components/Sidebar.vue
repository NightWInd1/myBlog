<template>
  <section class="comments-section" v-if="recentComments.length">
    <div class="comments-inner">
      <h2 class="section-title">最新留言</h2>
      <div class="comment-list">
        <div v-for="c in recentComments" :key="c.id" class="comment-item">
          <div class="comment-head">
            <span class="comment-author">{{ c.author_name }}</span>
            <span class="comment-time">{{ c.created_at?.slice(0, 10) }}</span>
          </div>
          <p class="comment-content">{{ c.content }}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="subscribe-section">
    <div class="subscribe-inner">
      <p class="subscribe-desc">♥ Subscribe</p>
      <p class="subscribe-hint">订阅博客，不错过任何更新。</p>
      <a href="/feed/" class="subscribe-btn">RSS 订阅</a>
    </div>
  </section>
</template>

<script setup>
defineProps({
  recentComments: { type: Array, default: () => [] }
})
</script>

<style scoped>
.comments-section {
  padding: 20px 0 60px;
}
.comments-inner {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 24px;
}

.comment-list {
  display: flex;
  flex-direction: column;
}
.comment-item {
  padding: 16px 0;
  border-bottom: 1px solid var(--color-border);
  transition: border-color 0.2s;
}
.comment-item:last-child { border-bottom: none; }
.comment-item:hover { border-color: var(--color-accent); }

.comment-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}
.comment-author {
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text);
}
.comment-time {
  font-size: 12px;
  color: var(--color-muted);
}
.comment-content {
  font-size: 14px;
  color: var(--color-text-secondary);
  line-height: 1.6;
}

.subscribe-section {
  padding: 0 0 60px;
}
.subscribe-inner {
  max-width: 680px;
  margin: 0 auto;
  padding: 32px 24px;
  text-align: center;
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  background: var(--color-bg-card);
}
.subscribe-desc {
  font-size: 18px;
  font-weight: 600;
  color: var(--color-accent);
  margin-bottom: 6px;
}
.subscribe-hint {
  font-size: 14px;
  color: var(--color-muted);
  margin-bottom: 16px;
}
.subscribe-btn {
  display: inline-flex;
  align-items: center;
  padding: 8px 24px;
  border-radius: var(--radius-sm);
  background: var(--color-accent);
  color: #fff;
  font-size: 14px;
  font-weight: 500;
  transition: background 0.2s;
}
.subscribe-btn:hover { background: var(--color-accent-hover); }
</style>
