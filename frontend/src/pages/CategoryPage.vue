<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useSite } from '../composables/useSite'
import PostCollection from '../components/PostCollection.vue'
import Icon from '../components/Icon.vue'
const route = useRoute()
const { flatCategories } = useSite()
const category = computed(() =>
  flatCategories.value.find((c) => c.slug === route.params.slug),
)
</script>
<template>
  <header class="page-heading panel">
    <span class="eyebrow">
      <Icon name="folder" :size="16" />
      CATEGORY
    </span>
    <h1>{{ category?.name || '文章分类' }}</h1>
    <p>{{ category?.description || '将零散的思绪，收藏在同一个角落。' }}</p>
    <div v-if="category?.children?.length" class="chip-list">
      <router-link
        v-for="child in category.children"
        :key="child.id"
        :to="`/category/${child.slug}`"
      >
        {{ child.name }}
        <small>{{ child.post_count }}</small>
      </router-link>
    </div>
  </header>
  <PostCollection :category="String(route.params.slug)" />
</template>
