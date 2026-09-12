<script setup>
import { onMounted, onUnmounted, ref } from 'vue'
import { site } from '../config/site'
import Icon from './Icon.vue'
defineProps({ compact: Boolean })
const parallax = ref(0)
const titleChars = [...'在晚风中，遇见生活的微光']
function updateParallax() {
  parallax.value = Math.min(window.scrollY * 0.14, 76)
}
onMounted(() => {
  window.addEventListener('scroll', updateParallax, { passive: true })
  updateParallax()
})
onUnmounted(() => window.removeEventListener('scroll', updateParallax))
function explore() {
  document.getElementById('main-content')?.scrollIntoView({
    behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches
      ? 'instant'
      : 'smooth',
    block: 'start',
  })
}
</script>
<template>
  <section class="hero" :class="{ compact }" aria-label="欢迎来到晚风如歌">
    <img
      class="hero-image"
      :src="site.heroImage"
      alt="樱花树下的二次元少女"
      fetchpriority="high"
      :style="{ transform: `translate3d(0, ${parallax}px, 0) scale(1.08)` }"
    />
    <div class="hero-shade"></div>
    <div class="hero-copy" v-if="!compact">
      <span class="hero-eyebrow">
        <span></span>
        A LITTLE CORNER OF MY WORLD
      </span>
      <h1 aria-label="在晚风中，遇见生活的微光">
        <template v-for="(char, index) in titleChars" :key="`${char}-${index}`">
          <br v-if="index === 4" class="mobile-break" />
          <span
            class="hero-char"
            :style="{ '--char-delay': `${120 + index * 58}ms` }"
          >{{ char }}</span>
        </template>
        <span class="hero-period">.</span>
      </h1>
      <p>{{ site.subtitle }}</p>
      <button class="explore-button" @click="explore">
        往下看看
        <Icon name="down" :size="16" />
      </button>
    </div>
    <div class="hero-bottom" v-if="!compact">
      <span>STAY CURIOUS. KEEP CREATING.</span>
      <span>ORIGINAL SAKURA NIGHT</span>
    </div>
    <svg
      class="hero-wave"
      viewBox="0 0 1440 65"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path
        class="wave-back"
        d="M0 30Q360 85 720 35T1440 30V65H0Z"
        fill="currentColor"
        opacity=".3"
      >
        <animate
          attributeName="d"
          dur="9s"
          repeatCount="indefinite"
          values="M0 30Q360 85 720 35T1440 30V65H0Z;M0 38Q360 12 720 42T1440 28V65H0Z;M0 30Q360 85 720 35T1440 30V65H0Z"
        />
      </path>
      <path
        class="wave-mid"
        d="M0 45Q360 3 720 43T1440 35V65H0Z"
        fill="currentColor"
        opacity=".5"
      >
        <animate
          attributeName="d"
          dur="7s"
          begin="-2s"
          repeatCount="indefinite"
          values="M0 45Q360 3 720 43T1440 35V65H0Z;M0 40Q360 73 720 34T1440 44V65H0Z;M0 45Q360 3 720 43T1440 35V65H0Z"
        />
      </path>
      <path class="wave-front" d="M0 54Q360 28 720 54T1440 48V65H0Z" fill="currentColor" />
    </svg>
  </section>
</template>
