<template>
  <button v-show="visible" type="button" class="back-to-top" @click="scrollTop" aria-label="回到顶部">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
  </button>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const visible = ref(false)
function onScroll() { visible.value = window.scrollY > 400 }
function scrollTop() { window.scrollTo({ top: 0, behavior: 'smooth' }) }

onMounted(() => window.addEventListener('scroll', onScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', onScroll))
</script>

<style scoped>
.back-to-top {
  position: fixed; bottom: 32px; right: 32px; z-index: 90;
  width: 40px; height: 40px; border-radius: 50%;
  background: var(--color-bg-card); border: 1px solid var(--color-border);
  color: var(--color-muted); cursor: pointer; display: flex;
  align-items: center; justify-content: center; transition: all .2s;
  box-shadow: 0 2px 8px rgba(0,0,0,.1);
}
.back-to-top:hover { color: var(--color-text); box-shadow: 0 4px 12px rgba(0,0,0,.15); }
</style>
