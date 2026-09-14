<script setup>
import { ref, computed, watch, nextTick, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppearance } from '../composables/useAppearance'
import { useSite } from '../composables/useSite'
import { site } from '../config/site'
import Icon from './Icon.vue'
const { theme, resolvedTheme, hue } = useAppearance()
const route = useRoute(),
  router = useRouter()
const { categories } = useSite()
const menuOpen = ref(false),
  settingsOpen = ref(false),
  query = ref(''),
  scrolled = ref(false),
  scrollDistance = ref(0),
  activeMenu = ref(''),
  submenuHovered = ref(false),
  submenuFading = ref(false),
  headerHidden = ref(false)
const searchInput = ref(null),
  dialog = ref(null),
  searchTrigger = ref(null)
let lastScrollY = 0
let submenuCloseTimer
const displaySiteName = computed(() => String(site.name || '').replace(/[.。．]+$/u, ''))
const categoryOrder = [
  { slug: 'life', text: '生活随笔' },
  { slug: 'devops', text: '运维部署' },
  { slug: 'posts', text: '文章' },
  { slug: 'memories', text: '记忆' },
  { slug: 'poetry', text: '诗词' },
  { slug: 'changes', text: '变化' },
  { slug: 'more', text: '更多' },
]
const nav = computed(() => {
  const lookup = new Map(categories.value.map((item) => [item.slug, item]))
  return [
    { slug: 'home', to: '/', text: '首页', icon: 'home', children: [] },
    ...categoryOrder.map((item) => ({
      ...item,
      to: `/category/${item.slug}`,
      icon: lookup.get(item.slug)?.icon || 'folder',
      children: lookup.get(item.slug)?.children || [],
    })),
  ]
})
function hasChildren(item) {
  return item.children?.length > 0
}
function toggleSubmenu(item) {
  window.clearTimeout(submenuCloseTimer)
  submenuFading.value = false
  activeMenu.value = activeMenu.value === item.slug ? '' : item.slug
}
function onSubmenuEnter() {
  submenuHovered.value = true
  submenuFading.value = false
  window.clearTimeout(submenuCloseTimer)
}
function scheduleSubmenuClose(delay = 420) {
  if (!activeMenu.value || submenuHovered.value) return
  if (submenuFading.value) return
  window.clearTimeout(submenuCloseTimer)
  submenuFading.value = true
  submenuCloseTimer = window.setTimeout(() => {
    if (!submenuHovered.value) {
      activeMenu.value = ''
      submenuFading.value = false
    }
  }, delay)
}
function onSubmenuLeave() {
  submenuHovered.value = false
  scheduleSubmenuClose()
}
function isActive(item) {
  return item.slug === 'home'
    ? route.path === '/'
    : route.path === item.to || route.path.startsWith(`${item.to}/`)
}
function goHome() {
  activeMenu.value = ''
  menuOpen.value = false
  router.push('/')
}
function handleNavClick(event, item) {
  if (item.slug === 'home') {
    event.preventDefault()
    goHome()
  }
}
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
  const currentY = Math.max(0, window.scrollY)
  const movingDown = currentY > lastScrollY + 2
  const movingUp = currentY < lastScrollY - 2
  scrolled.value = currentY > 60
  scrollDistance.value = Math.min(currentY / 260, 1)
  // Hide only after a meaningful downward movement. Once hidden, keep the
  // state while scrolling settles; reveal on upward movement or at the top.
  // Keep the tray available while the pointer is inside an open submenu.
  if (movingUp || currentY <= 60) {
    headerHidden.value = false
  } else if (movingDown && currentY > 120 && !submenuHovered.value) {
    headerHidden.value = true
  }
  if (activeMenu.value && !submenuHovered.value) {
    scheduleSubmenuClose(480)
  }
  lastScrollY = currentY
}
watch(
  () => route.fullPath,
  () => {
    menuOpen.value = settingsOpen.value = false
    activeMenu.value = ''
    submenuHovered.value = false
    submenuFading.value = false
  },
)
onMounted(() => {
  window.addEventListener('keydown', keydown)
  window.addEventListener('scroll', scroll, { passive: true })
  lastScrollY = window.scrollY
  scroll()
})
onUnmounted(() => {
  window.removeEventListener('keydown', keydown)
  window.removeEventListener('scroll', scroll)
  window.clearTimeout(submenuCloseTimer)
})
</script>
<template>
  <header
    class="site-header"
    :class="{ scrolled, 'header-hidden': headerHidden }"
    :style="{
      '--nav-lift': `${scrollDistance * -4}px`,
      '--nav-alpha': (0.42 + scrollDistance * 0.48).toFixed(2),
      '--nav-blur': `${12 + scrollDistance * 10}px`,
    }"
  >
    <div class="header-inner">
      <router-link class="brand" to="/" aria-label="晚风如歌首页" @click.prevent="goHome">
        <span class="brand-mark"><Icon name="leaf" :size="25" /></span>
        {{ displaySiteName }}
      </router-link>
      <nav class="desktop-nav" aria-label="主导航">
        <div
          v-for="item in nav"
          :key="item.slug"
          class="nav-item"
          :class="{ open: activeMenu === item.slug }"
        >
          <button
            v-if="hasChildren(item)"
            class="nav-link nav-parent"
            :class="{ active: isActive(item) }"
            type="button"
            :aria-expanded="activeMenu === item.slug"
            @click="toggleSubmenu(item)"
          >
            <Icon :name="item.icon" :size="17" />
            {{ item.text }}
            <Icon name="down" :size="12" />
          </button>
          <router-link
            v-else
            class="nav-link"
            :class="{ active: isActive(item) }"
            :to="item.to"
            @click="handleNavClick($event, item)"
          >
            <Icon :name="item.icon" :size="17" />
            {{ item.text }}
          </router-link>
            <TransitionGroup
            v-if="hasChildren(item) && activeMenu === item.slug"
            name="submenu"
            tag="div"
            class="nav-submenu"
            :class="{ 'submenu-fading': submenuFading }"
            @mouseenter="onSubmenuEnter"
            @mouseleave="onSubmenuLeave"
          >
            <router-link
              v-for="(child, index) in item.children"
              :key="child.id"
              :style="{ '--submenu-delay': `${index * 55}ms` }"
              :to="`/category/${child.slug}`"
            >
              {{ child.name }}
              <small>{{ child.post_count }}</small>
            </router-link>
          </TransitionGroup>
        </div>
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
          恢复樱花粉
        </button>
      </div>
      <nav
        id="mobile-nav"
        v-if="menuOpen"
        class="mobile-nav panel"
        aria-label="移动端导航"
      >
        <template v-for="item in nav" :key="item.slug">
          <button
            v-if="hasChildren(item)"
            class="mobile-nav-parent"
            type="button"
            :aria-expanded="activeMenu === item.slug"
            @click="toggleSubmenu(item)"
          >
            <span><Icon :name="item.icon" :size="18" />{{ item.text }}</span>
            <Icon :name="activeMenu === item.slug ? 'up' : 'down'" :size="15" />
          </button>
          <router-link
            v-else
            :to="item.to"
            @click="handleNavClick($event, item)"
          >
            <Icon :name="item.icon" :size="18" />
            {{ item.text }}
          </router-link>
          <TransitionGroup
            v-if="hasChildren(item) && activeMenu === item.slug"
            name="submenu"
            tag="div"
            class="mobile-submenu"
            :class="{ 'submenu-fading': submenuFading }"
            @mouseenter="onSubmenuEnter"
            @mouseleave="onSubmenuLeave"
          >
            <router-link
              v-for="(child, index) in item.children"
              :key="child.id"
              :style="{ '--submenu-delay': `${index * 55}ms` }"
              :to="`/category/${child.slug}`"
            >
              {{ child.name }}
              <small>{{ child.post_count }}</small>
            </router-link>
          </TransitionGroup>
        </template>
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
