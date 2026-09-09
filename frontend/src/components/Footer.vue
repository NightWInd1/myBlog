<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-grid">
        <div class="footer-col">
          <h4>关于</h4>
          <router-link to="/about">关于本站</router-link>
          <router-link to="/about">关于我</router-link>
        </div>
        <div class="footer-col">
          <h4>更多</h4>
          <router-link to="/">首页</router-link>
          <router-link to="/category/tech">技术笔记</router-link>
          <router-link to="/category/life">生活随笔</router-link>
        </div>
        <div class="footer-col">
          <h4>联系</h4>
          <a href="mailto:2163392313@qq.com">发送邮件</a>
          <a href="https://github.com/" target="_blank" rel="noopener">GitHub</a>
        </div>
      </div>

      <div class="footer-bottom">
        <div class="footer-brand">
          <router-link to="/" class="footer-logo">晚风</router-link>
          <span class="footer-motto">Stay hungry. Stay foolish.</span>
        </div>
        <div class="footer-copy">
          <span>&copy; 2024-2026</span>
          <span class="footer-dot">·</span>
          <span>Powered by Django &amp; Vue</span>
        </div>
        <div class="footer-links">
          <a href="/feed/">RSS Feed</a>
          <span class="footer-dot">·</span>
          <a href="/sitemap.xml">Sitemap</a>
        </div>
      </div>
    </div>
    <BackToTop />
  </footer>
</template>

<script setup>
import BackToTop from './BackToTop.vue'
</script>

<style scoped>
.site-footer {
  padding: 60px 0 40px;
  border-top: 1px solid var(--color-border);
  position: relative;
}
.footer-inner {
  max-width: 680px;
  margin: 0 auto;
  padding: 0 24px;
}

.footer-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  padding-bottom: 40px;
  margin-bottom: 32px;
  border-bottom: 1px solid var(--color-border);
}
.footer-col h4 {
  font-size: 13px;
  font-weight: 600;
  color: var(--color-text);
  margin-bottom: 12px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.footer-col a {
  display: block;
  font-size: 14px;
  color: var(--color-muted);
  padding: 3px 0;
  transition: color 0.2s;
}
.footer-col a:hover { color: var(--color-accent); }

.footer-bottom {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}
.footer-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}
.footer-logo {
  font-size: 20px;
  font-weight: 700;
  color: var(--color-text);
  transition: color 0.2s;
}
.footer-logo:hover { color: var(--color-accent); }
.footer-motto {
  font-size: 13px;
  color: var(--color-muted);
  font-style: italic;
}
.footer-copy {
  font-size: 12px;
  color: var(--color-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}
.footer-links {
  font-size: 12px;
  color: var(--color-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}
.footer-links a { color: var(--color-muted); transition: color 0.2s; }
.footer-links a:hover { color: var(--color-accent); }
.footer-dot { opacity: 0.4; }

@media (max-width: 480px) {
  .footer-grid { grid-template-columns: 1fr; gap: 20px; }
}
</style>
