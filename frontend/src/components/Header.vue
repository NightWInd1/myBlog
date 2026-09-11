<script setup>
import { ref, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppearance } from '../composables/useAppearance'
import { site } from '../config/site'
import Icon from './Icon.vue'
const { theme, resolvedTheme, hue } = useAppearance()
const route = useRoute(),
  router = useRouter()
const menuOpen = ref(false),
  settingsOpen = ref(false),
  query = ref(''),
  scrolled = ref(false)
const searchInput = ref(null),
  dialog = ref(null),
  searchTrigger = ref(null)
const nav = [
  { to: '/', text: '首页', icon: 'home' },
  { to: '/archives', text: '归档', icon: 'archive' },
  { to: '/categories', text: '分类', icon: 'folder' },
  { to: '/about', text: '关于', icon: 'info' },
]
async function openSearch() {
  menuOpen.value = settingsOpen.value = false
  await nextTick()
  dialog.value.showModal()
  searchInput.value?.focus()
}
function closeSearch() {
  dialog.value?.close()
  searchTrigger.value?.focus()
}
function search() {
  if (!query.value.trim()) return
  router.push({ path: '/search', query: { q: query.value.trim() } })
  closeSearch()
}
function keydown(e) {
  if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
    e.preventDefault()
    openSearch()
  }
  if (e.key === 'Escape') {
    settingsOpen.value = false
    menuOpen.value = false
  }
}
function toggleSettings() {
  settingsOpen.value = !settingsOpen.value
  menuOpen.value = false
}
function toggleMenu() {
  menuOpen.value = !menuOpen.value
  settingsOpen.value = false
}
function scroll() {
  scrolled.value = window.scrollY > 60
}
watch(
  () => route.fullPath,
  () => {
    menuOpen.value = settingsOpen.value = false
  },
)
onMounted(() => {
  window.addEventListener('keydown', keydown)
  window.addEventListener('scroll', scroll, { passive: true })
  scroll()
})
onUnmounted(() => {
  window.removeEventListener('keydown', keydown)
  window.removeEventListener('scroll', scroll)
})
</script>
<template>
  <header class="site-header" :class="{ scrolled }">
    <div class="header-inner">
      <router-link class="brand" to="/" aria-label="晚风的博客首页">
        <span class="brand-mark"><Icon name="leaf" :size="25" /></span>
        {{ site.name }}
        <span class="brand-dot">.</span>
      </router-link>
      <nav class="desktop-nav" aria-label="主导航">
        <router-link
          v-for="item in nav"
          :key="item.to"
          :to="item.to"
          :class="{
            active:
              item.to === '/'
                ? route.path === '/'
                : route.path.startsWith(item.to) ||
                  (item.to === '/categories' &&
                    route.path.startsWith('/category/')),
          }"
        >
          <Icon :name="item.icon" :size="17" />
          {{ item.text }}
        </router-link>
      </nav>
      <div class="header-actions">
        <button
          ref="searchTrigger"
          class="search-trigger"
          @click="openSearch"
          aria-label="搜索文章"
        >
          <Icon name="search" :size="18" />
          <span>搜索点什么…</span>
          <kbd>⌘ K</kbd>
        </button>
        <button
          class="icon-button"
          @click="toggleSettings"
          aria-label="外观设置"
          :aria-expanded="settingsOpen"
        >
          <Icon name="palette" />
        </button>
        <button
          class="icon-button theme-toggle"
          @click="theme = resolvedTheme === 'dark' ? 'light' : 'dark'"
          :aria-label="
            resolvedTheme === 'dark' ? '切换浅色模式' : '切换深色模式'
          "
        >
          <Icon :name="resolvedTheme === 'dark' ? 'moon' : 'sun'" />
        </button>
        <button
          class="icon-button mobile-menu-toggle"
          @click="toggleMenu"
          :aria-expanded="menuOpen"
          aria-controls="mobile-nav"
          aria-label="导航菜单"
        >
          <Icon :name="menuOpen ? 'close' : 'menu'" />
        </button>
      </div>
      <div v-if="settingsOpen" class="settings-panel panel">
        <div class="panel-heading">
          让这里更像你
          <button
            class="icon-button"
            @click="settingsOpen = false"
            aria-label="关闭外观设置"
          >
            <Icon name="close" :size="16" />
          </button>
        </div>
        <span class="settings-label">显示模式</span>
        <div class="theme-options">
          <button
            v-for="item in [
              { value: 'light', name: '浅色', icon: 'sun' },
              { value: 'dark', name: '深色', icon: 'moon' },
              { value: 'system', name: '自动', icon: 'monitor' },
            ]"
            :key="item.value"
            :class="{ selected: theme === item.value }"
            :aria-pressed="theme === item.value"
            @click="theme = item.value"
          >
            <Icon :name="item.icon" :size="18" />
            {{ item.name }}
          </button>
        </div>
        <label class="settings-label" for="theme-hue">
          主题色
          <span>{{ hue }}°</span>
        </label>
        <input
          id="theme-hue"
          type="range"
          min="0"
          max="360"
          v-model.number="hue"
          class="hue-slider"
        />
        <button class="text-button" @click="hue = site.defaultHue">
          恢复薄荷绿
        </button>
      </div>
      <nav
        id="mobile-nav"
        v-if="menuOpen"
        class="mobile-nav panel"
        aria-label="移动端导航"
      >
        <router-link v-for="item in nav" :to="item.to" :key="item.to">
          <Icon :name="item.icon" :size="18" />
          {{ item.text }}
        </router-link>
      </nav>
    </div>
  </header>
  <Teleport to="body">
    <dialog
      ref="dialog"
      class="search-dialog panel"
      @cancel.prevent="closeSearch"
      @click="
        (event) => {
          if (event.target === dialog) closeSearch()
        }
      "
      aria-labelledby="search-title"
    >
      <div class="search-dialog-heading">
        <h2 id="search-title">寻找一段文字</h2>
        <button class="icon-button" @click="closeSearch" aria-label="关闭搜索">
          <Icon name="close" />
        </button>
      </div>
      <form @submit.prevent="search">
        <Icon name="search" />
        <input
          ref="searchInput"
          v-model="query"
          placeholder="搜索文章、灵感、生活…"
          aria-label="搜索关键词"
        />
        <button class="primary-button" type="submit">
          搜索
          <Icon name="arrow" :size="16" />
        </button>
      </form>
      <p>
        搜索标题、摘要和正文
        <kbd>ESC 关闭</kbd>
      </p>
    </dialog>
  </Teleport>
</template>
