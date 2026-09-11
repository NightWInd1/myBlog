<script setup>
import { site } from '../config/site'
import { useSite } from '../composables/useSite'
import Icon from '../components/Icon.vue'
import Avatar from '../components/Avatar.vue'
const { stats } = useSite()
</script>
<template>
  <article class="panel about-panel">
    <div class="about-intro">
      <Avatar />
      <span class="eyebrow">A LITTLE ABOUT ME</span>
      <h1>
        你好，我是{{ site.author }}
        <span>.</span>
      </h1>
      <p>{{ site.subtitle }}</p>
    </div>
    <div class="about-stats">
      <div>
        <strong>{{ stats?.posts ?? '—' }}</strong>
        <span>篇生活记录</span>
      </div>
      <div>
        <strong>{{ stats?.categories ?? '—' }}</strong>
        <span>个探索方向</span>
      </div>
      <div>
        <strong>{{ stats?.comments ?? '—' }}</strong>
        <span>次文字相遇</span>
      </div>
    </div>
    <section class="about-section">
      <h2>
        <Icon name="leaf" />
        在代码与生活之间
      </h2>
      <p>一个热爱技术的全栈开发者，专注于 Python 后端开发和 Vue 前端工程化。</p>
      <p>
        喜欢探索新技术，也乐于分享学习过程中的经验和心得。这个博客是我的数字花园，用来记录技术笔记、生活随想，以及那些值得被记住的小事。
      </p>
      <blockquote>静水流深，闻喧享静。</blockquote>
    </section>
    <section class="about-section">
      <h2>
        <Icon name="spark" />
        我的工具箱
      </h2>
      <div class="skill-tags">
        <span v-for="skill in site.skills" :key="skill">{{ skill }}</span>
      </div>
    </section>
    <section class="about-section">
      <h2>
        <Icon name="mail" />
        让我们保持联系
      </h2>
      <p>如果这里的某段文字让你产生了共鸣，欢迎来打个招呼。</p>
      <div class="about-links">
        <a :href="site.github" target="_blank" rel="noopener noreferrer">
          <Icon name="github" :size="18" />
          GitHub
          <Icon name="arrow" :size="15" />
        </a>
        <a :href="`mailto:${site.email}`">
          <Icon name="mail" :size="18" />
          给我写信
          <Icon name="arrow" :size="15" />
        </a>
        <a href="/feed/">
          <Icon name="rss" :size="18" />
          订阅博客
          <Icon name="arrow" :size="15" />
        </a>
      </div>
    </section>
  </article>
</template>
