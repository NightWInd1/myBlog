<template>
  <div class="scroll-gradient" :style="{ opacity: gradientOpacity }"></div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const gradientOpacity = ref(0)

function onScroll() {
  const scrollY = window.scrollY
  const max = 300
  gradientOpacity.value = Math.min(scrollY / max, 1)
}

onMounted(() => {
  window.addEventListener('scroll', onScroll, { passive: true })
  document.documentElement.setAttribute('data-scrolling', '')
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
})
</script>

<style scoped>
.scroll-gradient {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 180px;
  z-index: 0;
  pointer-events: none;
  background: linear-gradient(
    180deg,
    var(--color-bg) 0%,
    color-mix(in srgb, var(--color-bg) 80%, transparent) 40%,
    transparent 100%
  );
}
[data-theme="dark"] .scroll-gradient {
  background: linear-gradient(
    180deg,
    var(--color-bg) 0%,
    color-mix(in srgb, var(--color-bg) 85%, transparent) 50%,
    transparent 100%
  );
}
</style>
