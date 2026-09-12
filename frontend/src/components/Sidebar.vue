<script setup>
import { useRoute } from 'vue-router'
import { useSite } from '../composables/useSite'
import { site } from '../config/site'
import Icon from './Icon.vue'
import Avatar from './Avatar.vue'
import MusicPlayer from './MusicPlayer.vue'
const { categories, stats, error, load } = useSite()
const route = useRoute()
</script>
<template>
  <aside class="left-sidebar" aria-label="博主和文章分类">
    <section class="panel profile-card">
      <div class="profile-cover">
        <span>HELLO, FRIEND</span>
        <Icon name="spark" :size="18" />
      </div>
      <router-link to="/about" class="profile-avatar" aria-label="了解晚风">
        <Avatar />
        <span class="online-dot"></span>
      </router-link>
      <h2>
        {{ site.author }}
        <span class="profile-leaf"><Icon name="leaf" :size="17" /></span>
      </h2>
      <span class="profile-english">{{ site.englishName }}</span>
      <p class="profile-bio">{{ site.bio }}</p>
      <div class="profile-stats">
        <router-link to="/archives">
          <strong>{{ stats?.posts ?? '—' }}</strong>
          <span>文章</span>
        </router-link>
        <router-link to="/categories">
          <strong>{{ stats?.categories ?? '—' }}</strong>
          <span>分类</span>
        </router-link>
        <router-link to="/about">
          <strong>{{ stats?.comments ?? '—' }}</strong>
          <span>留言</span>
        </router-link>
      </div>
      <div class="social-links">
        <a
          :href="site.github"
          target="_blank"
          rel="noopener noreferrer"
          aria-label="GitHub"
        >
          <Icon name="github" :size="19" />
        </a>
        <a :href="`mailto:${site.email}`" aria-label="发送邮件">
          <Icon name="mail" :size="19" />
        </a>
        <a href="/feed/" aria-label="RSS 订阅">
          <Icon name="rss" :size="19" />
        </a>
      </div>
    </section>
    <MusicPlayer />
    <section class="panel announcement-card">
      <h2 class="widget-title">
        <Icon name="spark" :size="18" />
        小站公告
      </h2>
      <p>{{ site.announcement }}</p>
      <router-link to="/about" class="subtle-link">
        很高兴认识你
        <Icon name="arrow" :size="15" />
      </router-link>
    </section>
    <section class="panel category-widget">
      <h2 class="widget-title">
        <Icon name="folder" :size="18" />
        文章分类
        <router-link to="/categories" aria-label="查看全部分类">
          <Icon name="chevron" :size="15" />
        </router-link>
      </h2>
      <p v-if="error && !categories.length" class="muted">
        分类加载失败
        <button class="text-button" @click="load">重试</button>
      </p>
      <router-link
        v-for="cat in categories"
        :key="cat.id"
        :to="`/category/${cat.slug}`"
        class="category-row"
        :class="{ selected: route.params.slug === cat.slug }"
      >
        <span>{{ cat.icon || '⌑' }}</span>
        <span>{{ cat.name }}</span>
        <small>{{ cat.post_count }}</small>
      </router-link>
    </section>
    <div class="sidebar-note">
      <Icon name="leaf" :size="16" />
      慢慢来，好的故事值得等待。
    </div>
  </aside>
</template>
