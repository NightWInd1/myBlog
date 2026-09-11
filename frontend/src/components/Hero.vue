<script setup>
import { site } from '../config/site'
import Icon from './Icon.vue'
defineProps({ compact: Boolean })
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
  <section class="hero" :class="{ compact }" aria-label="欢迎来到晚风的博客">
    <img
      class="hero-image"
      :src="site.heroImage"
      alt="群山环绕着平静的湖泊，山间小屋倒映在水面"
      fetchpriority="high"
    />
    <div class="hero-shade"></div>
    <div class="hero-copy" v-if="!compact">
      <span class="hero-eyebrow">
        <span></span>
        A LITTLE CORNER OF MY WORLD
      </span>
      <h1>
        在晚风中，
        <br class="mobile-break" />
        遇见生活的微光
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
      <span>{{ site.heroCredit }}</span>
    </div>
    <svg
      class="hero-wave"
      viewBox="0 0 1440 65"
      preserveAspectRatio="none"
      aria-hidden="true"
    >
      <path
        d="M0 30Q360 85 720 35T1440 30V65H0Z"
        fill="currentColor"
        opacity=".3"
      />
      <path
        d="M0 45Q360 3 720 43T1440 35V65H0Z"
        fill="currentColor"
        opacity=".5"
      />
      <path d="M0 54Q360 28 720 54T1440 48V65H0Z" fill="currentColor" />
    </svg>
  </section>
</template>
