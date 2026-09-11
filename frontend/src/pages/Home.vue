<script setup>
import { computed } from 'vue'
import { useSite } from '../composables/useSite'
import Icon from '../components/Icon.vue'
import PostCollection from '../components/PostCollection.vue'
const { categories } = useSite()
const shortcuts = computed(() =>
  [...categories.value].sort((a, b) => b.post_count - a.post_count).slice(0, 4),
)
</script>
<template>
  <nav class="category-bar panel" aria-label="快捷分类">
    <router-link to="/" class="selected">
      <Icon name="home" :size="16" />
      全部文章
    </router-link>
    <router-link
      v-for="cat in shortcuts"
      :key="cat.id"
      :to="`/category/${cat.slug}`"
    >
      {{ cat.name }}
      <small>{{ cat.post_count }}</small>
    </router-link>
    <router-link to="/categories" class="category-more" aria-label="更多分类">
      <Icon name="chevron" :size="17" />
    </router-link>
  </nav>
  <div class="welcome-line">
    <span>
      <span class="status-dot"></span>
      生活明朗，万物可爱。
    </span>
    <span>WELCOME TO MY BLOG</span>
  </div>
  <PostCollection />
</template>
