<script setup>
import Icon from '../components/Icon.vue'
</script>
<template>
  <div class="panel empty-state not-found">
    <span>404</span>
    <h1>这阵风，吹向了别处</h1>
    <p>你寻找的页面不存在，回到首页继续探索吧。</p>
    <router-link to="/" class="primary-button">
      回到首页
      <Icon name="arrow" :size="16" />
    </router-link>
  </div>
</template>
