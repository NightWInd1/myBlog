<script setup>
import { computed } from 'vue'
const petals = computed(() =>
  Array.from({ length: 30 }, (_, i) => ({
    id: i,
    left: `${(i * 37) % 101}%`,
    delay: `${-((i * 1.71) % 14)}s`,
    duration: `${8 + (i % 7) * 1.35}s`,
    size: `${7 + (i % 4) * 2}px`,
    drift: `${-80 + (i % 9) * 20}px`,
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
