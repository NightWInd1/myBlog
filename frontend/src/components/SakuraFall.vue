<script setup>
import { computed } from 'vue'
const petals = computed(() =>
  Array.from({ length: 42 }, (_, i) => ({
    id: i,
    left: `${(i * 37) % 101}%`,
    delay: `${-((i * 1.71) % 17)}s`,
    duration: `${10 + (i % 8) * 1.45}s`,
    size: `${6 + (i % 5) * 2}px`,
    drift: `${-105 + (i % 11) * 21}px`,
    rotate: `${(i * 43) % 360}deg`,
  })),
)
</script>
<template>
  <div class="sakura-layer" aria-hidden="true">
    <i
      v-for="petal in petals"
      :key="petal.id"
      class="sakura-petal"
      :style="{
        left: petal.left,
        animationDelay: petal.delay,
        animationDuration: petal.duration,
        width: petal.size,
        height: `calc(${petal.size} * 1.45)`,
        '--drift': petal.drift,
        '--rotate': petal.rotate,
      }"
    ></i>
  </div>
</template>
