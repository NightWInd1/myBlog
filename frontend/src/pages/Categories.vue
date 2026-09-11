<script setup>
import { useSite } from '../composables/useSite'
import Icon from '../components/Icon.vue'
const { categories, loading, error, load } = useSite()
</script>
<template>
  <header class="page-heading panel">
    <span class="eyebrow">
      <Icon name="folder" :size="16" />
      COLLECTIONS
    </span>
    <h1>
      文字的不同切面
      <span>.</span>
    </h1>
    <p>关于技术，关于生活，也关于那些转瞬即逝的灵感。</p>
  </header>
  <div v-if="loading" class="panel empty-state" role="status">
    正在整理分类…
  </div>
  <div v-else-if="error && !categories.length" class="panel empty-state">
    <p>分类暂时加载失败。</p>
    <button class="primary-button" @click="load">重试</button>
  </div>
  <div v-else-if="!categories.length" class="panel empty-state">
    还没有分类。
  </div>
  <div v-else class="category-cards">
    <section
      v-for="cat in categories"
      :key="cat.id"
      class="panel category-group"
    >
      <router-link :to="`/category/${cat.slug}`" class="category-group-heading">
        <span class="category-symbol">{{ cat.icon || '⌑' }}</span>
        <h2>{{ cat.name }}</h2>
        <span>
          {{ cat.post_count }} 篇
          <Icon name="chevron" :size="15" />
        </span>
      </router-link>
      <p>{{ cat.description || '收藏一点思考，留住一些日常。' }}</p>
      <div class="chip-list">
        <router-link
          v-for="child in cat.children"
          :key="child.id"
          :to="`/category/${child.slug}`"
        >
          {{ child.name }}
          <small>{{ child.post_count }}</small>
        </router-link>
      </div>
    </section>
  </div>
</template>
