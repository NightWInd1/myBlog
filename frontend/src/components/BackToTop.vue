<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Icon from './Icon.vue'
const visible = ref(false),
  progress = ref(0)
function update() {
  visible.value = window.scrollY > 300
  const max = document.documentElement.scrollHeight - window.innerHeight
  progress.value =
    max > 0 ? Math.min(100, Math.round((window.scrollY / max) * 100)) : 0
}
function top() {
  window.scrollTo({
    top: 0,
    behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches
      ? 'instant'
      : 'smooth',
  })
}
onMounted(() => {
  window.addEventListener('scroll', update, { passive: true })
  update()
})
onUnmounted(() => window.removeEventListener('scroll', update))
</script>
<template>
  <button
    v-if="visible"
    class="back-to-top panel"
    @click="top"
    aria-label="返回顶部"
  >
    <Icon name="up" :size="20" />
    <span>{{ progress }}%</span>
  </button>
</template>
