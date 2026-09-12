<script setup>
import { onMounted } from 'vue'
import { useRoute } from 'vue-router'
import Header from './components/Header.vue'
import Hero from './components/Hero.vue'
import Sidebar from './components/Sidebar.vue'
import RightSidebar from './components/RightSidebar.vue'
import Footer from './components/Footer.vue'
import BackToTop from './components/BackToTop.vue'
import SakuraFall from './components/SakuraFall.vue'
import ParticleField from './components/ParticleField.vue'
import { useSite } from './composables/useSite'
const route = useRoute()
const { load } = useSite()
onMounted(load)
</script>
<template>
  <ParticleField />
  <SakuraFall />
  <a href="#main-content" class="skip-link">跳转到正文</a>
  <Header />
  <Hero :key="route.name" :compact="route.name !== 'Home'" />
  <div class="site-layout" :class="{ 'inner-layout': route.name !== 'Home' }">
    <Sidebar />
    <main id="main-content" class="main-content" tabindex="-1">
      <router-view v-slot="{ Component }">
        <component :is="Component" />
      </router-view>
    </main>
    <RightSidebar />
  </div>
  <Footer />
  <BackToTop />
</template>
