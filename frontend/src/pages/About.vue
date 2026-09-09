<template>
  <div class="site-shell">
    <ScrollGradient />
    <Header />
    <main class="page-main">
      <div class="container">
        <div class="about-header">
          <div class="about-avatar-wrap">
            <svg class="about-avatar-svg" viewBox="0 0 100 100" fill="none">
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
            </svg>
          </div>
          <h1>晚风</h1>
          <p class="about-bio">一个混迹在IT行业的小菜鸟</p>
        </div>

        <div class="about-stats">
          <div class="stat-item"><strong>12</strong><span>文章</span></div>
          <div class="stat-item"><strong>3</strong><span>分类</span></div>
          <div class="stat-item"><strong>17</strong><span>评论</span></div>
        </div>

        <div class="about-section">
          <h2>关于我</h2>
          <p>一个热爱技术的全栈开发者，专注于 Python 后端开发和 Vue 前端工程化。</p>
          <p>喜欢探索新技术，乐于分享学习过程中的经验和心得。这个博客用来记录技术笔记和生活随想。</p>
        </div>

        <div class="about-section">
          <h2>技能</h2>
          <div class="skill-tags">
            <span>Python</span><span>Django</span><span>Vue.js</span><span>JavaScript</span>
            <span>Docker</span><span>Linux</span><span>Git</span><span>SQL</span>
          </div>
        </div>

        <div class="about-section">
          <h2>联系我</h2>
          <div class="contact-links">
            <a href="mailto:2163392313@qq.com">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/></svg>
              邮箱
            </a>
            <a href="https://github.com/" target="_blank" rel="noopener">
              <svg viewBox="0 0 24 24" fill="currentColor" width="16" height="16"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
              GitHub
            </a>
            <a href="/feed/">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 11a9 9 0 0 1 9 9"/><path d="M4 4a16 16 0 0 1 16 16"/><circle cx="5" cy="19" r="1"/></svg>
              RSS
            </a>
          </div>
        </div>
      </div>
    </main>
    <Footer />
  </div>
</template>

<script setup>
import ScrollGradient from '../components/ScrollGradient.vue'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
.page-main { padding: 100px 0 60px; }
.container { max-width: 680px; margin: 0 auto; padding: 0 24px; }

.about-header { text-align: center; padding-bottom: 32px; }
.about-avatar-wrap { margin-bottom: 16px; }
.about-avatar-svg {
  width: 96px; height: 96px; border-radius: 50%;
  border: 2px solid var(--color-border);
}
.about-header h1 { font-size: 26px; font-weight: 800; color: var(--color-text); margin: 0 0 6px; }
.about-bio { font-size: 15px; color: var(--color-muted); margin: 0; }

.about-stats { display: flex; justify-content: center; gap: 40px; padding: 20px 0; border-top: 1px solid var(--color-border); border-bottom: 1px solid var(--color-border); margin-bottom: 32px; }
.stat-item { display: flex; flex-direction: column; align-items: center; }
.stat-item strong { font-size: 22px; color: var(--color-text); }
.stat-item span { font-size: 12px; color: var(--color-muted); }

.about-section { margin-bottom: 32px; }
.about-section h2 { font-size: 18px; font-weight: 700; margin: 0 0 14px; color: var(--color-text); }
.about-section p { font-size: 14px; line-height: 1.8; color: var(--color-text-secondary); margin: 0 0 6px; }

.skill-tags { display: flex; flex-wrap: wrap; gap: 8px; }
.skill-tags span {
  font-size: 12px; padding: 4px 12px; border-radius: 20px;
  background: var(--color-accent-soft); color: var(--color-accent);
  font-weight: 500;
}

.contact-links { display: flex; flex-wrap: wrap; gap: 10px; }
.contact-links a {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 8px 18px; border-radius: var(--radius-sm);
  background: var(--color-bg-secondary); color: var(--color-text);
  font-size: 14px; font-weight: 500; transition: all 0.2s;
}
.contact-links a:hover { background: var(--color-accent); color: #fff; }
</style>
