<template>
  <section class="hero">
    <div class="hero-inner">
      <div class="hero-avatar-wrap">
        <div class="hero-avatar-ring"></div>
        <div class="hero-avatar-stack">
          <svg class="hero-avatar-svg" viewBox="0 0 100 100" fill="none">
            <circle cx="50" cy="50" r="50" fill="#f0d9b5"/>
            <ellipse cx="50" cy="95" rx="38" ry="18" fill="#2d2d2d"/>
            <path d="M22 50 Q50 18 78 50" stroke="#2d2d2d" stroke-width="1.8" fill="none"/>
            <circle cx="38" cy="46" r="5.5" fill="#2d2d2d"/>
            <circle cx="62" cy="46" r="5.5" fill="#2d2d2d"/>
            <circle cx="40" cy="44" r="2" fill="#fff"/>
            <circle cx="64" cy="44" r="2" fill="#fff"/>
            <path d="M38 62 Q50 72 62 62" stroke="#d4887a" stroke-width="2.5" fill="none" stroke-linecap="round"/>
            <ellipse cx="58" cy="32" rx="5.5" ry="3.5" fill="#f4a460" transform="rotate(-15 58 32)"/>
            <ellipse cx="40" cy="30" rx="5" ry="3" fill="#f4a460" transform="rotate(10 40 30)"/>
            <ellipse cx="20" cy="56" rx="6" ry="3" fill="#f4a460" transform="rotate(-20 20 56)"/>
          </svg>
          <svg class="hero-term-svg" viewBox="0 0 40 40" fill="none">
            <rect x="3" y="6" width="34" height="28" rx="6" fill="#1c1c1e" stroke="#555" stroke-width="1.5"/>
            <circle cx="10" cy="14" r="2.5" fill="#ff5f56"/>
            <circle cx="18" cy="14" r="2.5" fill="#ffbd2e"/>
            <circle cx="26" cy="14" r="2.5" fill="#27c93f"/>
            <rect x="6" y="22" width="16" height="2.5" rx="1.2" fill="#58a6ff"/>
            <rect x="6" y="27" width="10" height="2" rx="1" fill="#8b949e" opacity="0.5"/>
          </svg>
        </div>
      </div>

      <h1 class="hero-greeting">
        Hi，我是 <span class="hero-name">晚风</span>
        <span class="hero-emoji">👋</span>
      </h1>

      <p class="hero-tagline">
        I build things with <span class="hero-accent">✦ Code & Thought</span>
      </p>

      <p class="hero-bio">
        一个热爱技术的全栈开发者，探索代码世界，思考产品逻辑。
      </p>

      <p class="hero-quote">
        「静水流深，闻喧享静。」
      </p>

      <div class="hero-stats" v-if="stats">
        <span>{{ stats.posts }} 篇文章</span>
        <span class="stat-dot">·</span>
        <span>{{ stats.categories }} 个分类</span>
        <span class="stat-dot">·</span>
        <span>{{ stats.comments }} 条评论</span>
      </div>

      <div class="hero-social">
        <a href="https://github.com/" target="_blank" rel="noopener" title="GitHub">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
        </a>
        <a href="mailto:2163392313@qq.com" title="Email">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
        </a>
        <a href="/feed/" title="RSS">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11a9 9 0 0 1 9 9"/><path d="M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1"/></svg>
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  stats: { type: Object, default: () => ({ posts: 0, categories: 0, comments: 0 }) }
})
</script>

<style scoped>
.hero {
  padding: 120px 0 60px;
  position: relative;
}
.hero-inner {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.hero-avatar-wrap {
  position: relative;
  margin-bottom: 28px;
}
.hero-avatar-ring {
  position: absolute;
  inset: -5px;
  border-radius: 50%;
  background: conic-gradient(from 0deg, var(--color-accent), var(--color-border), var(--color-accent), var(--color-border));
  opacity: 0.4;
  animation: avatarSpin 6s linear infinite;
}
@keyframes avatarSpin {
  to { transform: rotate(360deg); }
}
.hero-avatar-stack {
  position: relative;
  width: 100px;
  height: 100px;
  z-index: 1;
}
.hero-avatar-svg {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  border: 3px solid var(--color-bg);
  box-shadow: 0 0 0 1px var(--color-border);
}
.hero-term-svg {
  position: absolute;
  bottom: -4px;
  right: -6px;
  width: 36px;
  height: 36px;
  filter: drop-shadow(0 2px 4px rgba(0,0,0,0.12));
}

.hero-greeting {
  font-size: 28px;
  font-weight: 700;
  line-height: 1.3;
  color: var(--color-text);
}
.hero-name {
  color: var(--color-accent);
}
.hero-emoji {
  display: inline-block;
  animation: wave 2s ease-in-out infinite;
  transform-origin: 70% 70%;
}
@keyframes wave {
  0%, 100% { transform: rotate(0deg); }
  25% { transform: rotate(14deg); }
  75% { transform: rotate(-8deg); }
}

.hero-tagline {
  margin-top: 12px;
  font-size: 17px;
  color: var(--color-text-secondary);
}
.hero-accent {
  font-weight: 600;
  background: linear-gradient(135deg, var(--color-accent), #d4856b);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-bio {
  margin-top: 14px;
  font-size: 14px;
  color: var(--color-muted);
  max-width: 440px;
}

.hero-quote {
  margin-top: 22px;
  font-size: 15px;
  color: var(--color-muted);
  font-style: italic;
}

.hero-stats {
  margin-top: 22px;
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--color-muted);
}
.stat-dot { opacity: 0.4; }

.hero-social {
  margin-top: 24px;
  display: flex;
  align-items: center;
  gap: 4px;
}
.hero-social a {
  width: 38px; height: 38px;
  display: flex; align-items: center; justify-content: center;
  border-radius: var(--radius-sm);
  color: var(--color-muted);
  transition: color 0.2s, background 0.2s;
}
.hero-social a:hover {
  color: var(--color-accent);
  background: var(--color-accent-soft);
}
.hero-social svg {
  width: 19px; height: 19px;
}

@media (max-width: 768px) {
  .hero { padding: 100px 0 40px; }
  .hero-greeting { font-size: 23px; }
  .hero-tagline { font-size: 15px; }
  .hero-avatar-stack { width: 84px; height: 84px; }
  .hero-avatar-svg { width: 84px; height: 84px; border-width: 2px; }
  .hero-term-svg { width: 30px; height: 30px; bottom: -3px; right: -4px; }
}
</style>
