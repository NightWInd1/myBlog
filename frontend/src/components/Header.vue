<template>
  <header class="site-header" :class="{ 'is-scrolled': scrolled, 'has-dropdown': activeDropdown }">
    <div class="header-inner">
      <router-link class="brand" to="/">
        <div class="brand-icon">
          <svg class="brand-avatar" viewBox="0 0 48 48" fill="none">
            <defs>
              <clipPath id="avatarClip"><circle cx="24" cy="24" r="24"/></clipPath>
            </defs>
            <circle cx="24" cy="24" r="24" fill="#f0d9b5"/>
            <g clip-path="url(#avatarClip)">
              <ellipse cx="24" cy="48" rx="20" ry="12" fill="#2d2d2d"/>
              <ellipse cx="24" cy="52" rx="10" ry="8" fill="#222"/>
              <path d="M10 24 Q24 10 38 24" stroke="#2d2d2d" stroke-width="1" fill="none"/>
              <circle cx="18" cy="22" r="3" fill="#2d2d2d"/>
              <circle cx="30" cy="22" r="3" fill="#2d2d2d"/>
              <circle cx="19" cy="21" r="1" fill="#fff"/>
              <circle cx="31" cy="21" r="1" fill="#fff"/>
              <path d="M18 30 Q24 36 30 30" stroke="#d4887a" stroke-width="1.5" fill="none" stroke-linecap="round"/>
              <ellipse cx="28" cy="16" rx="3" ry="2" fill="#f4a460" transform="rotate(-15 28 16)"/>
              <ellipse cx="18" cy="14" rx="3" ry="2" fill="#f4a460" transform="rotate(10 18 14)"/>
            </g>
          </svg>
          <svg class="brand-terminal" viewBox="0 0 32 32" fill="none">
            <rect x="2" y="4" width="28" height="24" rx="5" fill="#1c1c1e" stroke="#555" stroke-width="1.5"/>
            <circle cx="9" cy="11" r="2" fill="#ff5f56"/>
            <circle cx="16" cy="11" r="2" fill="#ffbd2e"/>
            <circle cx="23" cy="11" r="2" fill="#27c93f"/>
            <rect x="5" y="17" width="14" height="2" rx="1" fill="#58a6ff"/>
            <rect x="5" y="22" width="8" height="2" rx="1" fill="#8b949e" opacity="0.6"/>
          </svg>
        </div>
        <span class="brand-text">晚风</span>
      </router-link>

      <nav class="site-nav" :class="{ 'is-open': menuOpen }">
        <router-link to="/" class="nav-link-direct" @click="closeAll" exact-active-class="router-link-active">首页</router-link>
        <div
          v-for="item in navItems"
          :key="item.key"
          class="nav-item"
          :class="{ 'is-active': activeDropdown === item.key }"
        >
          <button class="nav-trigger" @click="toggleDropdown(item.key)">
            <span>{{ item.label }}</span>
            <svg class="nav-chevron" width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="6 9 12 15 18 9"/></svg>
          </button>
        </div>
      </nav>

      <div class="header-actions">
        <button class="search-btn" @click="focusSearch" title="搜索 (Ctrl+K)">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
          </svg>
        </button>
        <button class="theme-btn" @click="toggleTheme" :title="theme === 'dark' ? '浅色模式' : '深色模式'">
          <svg v-if="theme === 'dark'" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
          </svg>
          <svg v-else width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/>
          </svg>
        </button>
        <button class="nav-toggle" :class="{ 'is-active': menuOpen }" @click="menuOpen = !menuOpen" aria-label="菜单">
          <span></span><span></span>
        </button>
      </div>
    </div>

    <transition name="dropdown-fade">
      <div v-if="activeDropdown" class="nav-dropdown" @mouseleave="activeDropdown = null">
        <div class="dropdown-inner">

          <router-link
            v-for="child in activeCategoryChildren"
            :key="child.id"
            :to="`/category/${child.slug}`"
            class="dropdown-link"
            @click="closeAll"
          >
            <span class="dropdown-icon" v-if="child.icon">{{ child.icon }}</span>
            <div>
              <strong>{{ child.name }}</strong>
              <small v-if="child.description">{{ child.description }}</small>
            </div>
          </router-link>

          <template v-if="activeDropdown === 'more'">
            <a href="https://github.com/NightWInd1?tab=repositories" target="_blank" rel="noopener" class="dropdown-link" @click="closeAll">
              <span class="dropdown-icon">🐙</span>
              <div>
                <strong>GitHub 主页 <svg class="dropdown-external" width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></strong>
                <small>NightWInd1 · 开源项目</small>
              </div>
            </a>
          </template>

        </div>
      </div>
    </transition>

    <Teleport to="body">
      <div class="search-overlay" v-if="searchOpen" @click.self="searchOpen = false">
        <div class="search-modal">
          <form @submit.prevent="onSearch">
            <input ref="searchInputRef" v-model="searchQuery" type="text" placeholder="搜索文章..." autofocus />
            <kbd>ESC</kbd>
          </form>
        </div>
      </div>
    </Teleport>
  </header>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '../api.js'

const router = useRouter()
const scrolled = ref(false)
const menuOpen = ref(false)
const searchOpen = ref(false)
const searchQuery = ref('')
const searchInputRef = ref(null)
const theme = ref('light')
const activeDropdown = ref(null)
const categories = ref([])

const navItems = ref([])

const activeCategoryChildren = computed(() => {
  const cat = categories.value.find(c => c.slug === activeDropdown.value)
  return cat ? cat.children : []
})

async function fetchCategories() {
  try {
    const data = await api.get('/api/categories/')
    categories.value = data
    navItems.value = data.map(cat => ({
      key: cat.slug,
      label: cat.name,
    }))
  } catch (e) {
    console.error('Failed to fetch categories:', e)
  }
}

function toggleDropdown(key) {
  activeDropdown.value = activeDropdown.value === key ? null : key
}
function closeAll() {
  activeDropdown.value = null
  menuOpen.value = false
}

function onScroll() { scrolled.value = window.scrollY > 20 }
function toggleTheme() {
  theme.value = theme.value === 'dark' ? 'light' : 'dark'
  document.documentElement.setAttribute('data-theme', theme.value)
  localStorage.setItem('blog-theme', theme.value)
}

function focusSearch() { searchOpen.value = true; searchQuery.value = '' }
function onSearch() {
  if (!searchQuery.value.trim()) return
  router.push(`/search?q=${encodeURIComponent(searchQuery.value.trim())}`)
  searchOpen.value = false
}

function onKeydown(e) {
  if ((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); focusSearch() }
  if (e.key === 'Escape') { searchOpen.value = false; activeDropdown.value = null }
}

onMounted(() => {
  theme.value = document.documentElement.getAttribute('data-theme') || 'light'
  window.addEventListener('scroll', onScroll, { passive: true })
  window.addEventListener('keydown', onKeydown)
  fetchCategories()
})
onUnmounted(() => {
  window.removeEventListener('scroll', onScroll)
  window.removeEventListener('keydown', onKeydown)
})
</script>

<style scoped>
.site-header {
  position: fixed;
  top: 0; left: 0; right: 0;
  z-index: 100;
  background: var(--color-bg);
  transition: background 0.3s, box-shadow 0.3s;
}
.site-header.is-scrolled {
  box-shadow: 0 1px 0 var(--color-border);
}
.site-header.has-dropdown {
  background: var(--color-bg);
  box-shadow: 0 1px 0 var(--color-border);
}

.header-inner {
  max-width: 820px;
  margin: 0 auto;
  padding: 0 20px;
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.brand {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
  transition: opacity 0.2s;
}
.brand:hover { opacity: 0.8; }

.brand-icon {
  position: relative;
  width: 32px;
  height: 32px;
  flex-shrink: 0;
}
.brand-avatar {
  width: 32px; height: 32px;
  border-radius: 50%;
  position: relative; z-index: 1;
  border: 1.5px solid var(--color-border);
}
.brand-terminal {
  width: 16px; height: 16px;
  position: absolute;
  bottom: -2px; right: -4px;
  z-index: 2;
  filter: drop-shadow(0 1px 2px rgba(0,0,0,0.15));
}
.brand-text {
  font-size: 16px; font-weight: 700;
  color: var(--color-text);
  letter-spacing: 0.03em;
}

.site-nav {
  display: flex;
  align-items: center;
  gap: 2px;
}

.nav-link-direct {
  font-size: 14px;
  padding: 6px 10px;
  border-radius: var(--radius-sm);
  color: var(--color-muted);
  transition: color 0.2s, background 0.2s;
}
.nav-link-direct:hover,
.nav-link-direct.router-link-active {
  color: var(--color-text);
  background: var(--color-bg-hover);
}

.nav-item { position: relative; }
.nav-trigger {
  display: flex; align-items: center; gap: 4px;
  padding: 6px 10px; border-radius: var(--radius-sm);
  font-size: 14px; color: var(--color-muted);
  transition: color 0.2s, background 0.2s;
}
.nav-trigger:hover,
.nav-item.is-active .nav-trigger {
  color: var(--color-text);
  background: var(--color-bg-hover);
}
.nav-chevron { transition: transform 0.2s; }
.nav-item.is-active .nav-chevron { transform: rotate(180deg); }

.header-actions {
  display: flex; align-items: center; gap: 2px;
  flex-shrink: 0;
}
.search-btn, .theme-btn {
  width: 34px; height: 34px;
  display: flex; align-items: center; justify-content: center;
  border-radius: var(--radius-sm);
  color: var(--color-muted);
  transition: color 0.2s, background 0.2s;
}
.search-btn:hover, .theme-btn:hover {
  color: var(--color-text);
  background: var(--color-bg-hover);
}
.nav-toggle { display: none; }

.nav-dropdown {
  position: absolute;
  top: 56px; left: 0; right: 0;
  background: var(--color-bg);
  border-bottom: 1px solid var(--color-border);
  box-shadow: 0 8px 24px rgba(0,0,0,0.06);
  z-index: 99;
  padding: 24px 0;
}
.dropdown-inner {
  max-width: 820px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 6px;
}
.dropdown-link {
  display: flex; align-items: center; gap: 12px;
  padding: 12px 14px; border-radius: var(--radius-md);
  transition: background 0.15s;
}
.dropdown-link:hover { background: var(--color-bg-hover); }
.dropdown-link > div {
  display: flex; flex-direction: column; gap: 2px;
}
.dropdown-link strong {
  font-size: 14px; font-weight: 600;
  color: var(--color-text);
  display: flex; align-items: center; gap: 6px;
}
.dropdown-link small {
  font-size: 12px; color: var(--color-muted);
}
.dropdown-icon {
  font-size: 22px; width: 32px; text-align: center;
  flex-shrink: 0;
}
.dropdown-external {
  color: var(--color-muted); flex-shrink: 0;
}

.dropdown-fade-enter-active { transition: all 0.2s ease; }
.dropdown-fade-leave-active { transition: all 0.15s ease; }
.dropdown-fade-enter-from,
.dropdown-fade-leave-to {
  opacity: 0; transform: translateY(-8px);
}

.search-overlay {
  position: fixed; inset: 0; z-index: 200;
  background: rgba(0,0,0,0.3);
  backdrop-filter: blur(4px);
  display: flex; justify-content: center;
  padding-top: 15vh;
}
.search-modal {
  width: 560px; max-width: 92vw;
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  box-shadow: 0 16px 48px rgba(0,0,0,0.18);
}
.search-modal form {
  display: flex; align-items: center;
  padding: 14px 16px;
}
.search-modal input {
  flex: 1; border: none; background: none;
  font-size: 16px; color: var(--color-text);
  outline: none; font-family: inherit;
}
.search-modal input::placeholder { color: var(--color-muted); }
.search-modal kbd {
  font-size: 11px; padding: 2px 7px;
  border-radius: 4px;
  background: var(--color-bg-secondary);
  color: var(--color-muted);
  border: 1px solid var(--color-border);
}

@media (max-width: 768px) {
  .site-nav {
    display: none;
    position: fixed; top: 56px; left: 0; right: 0;
    background: var(--color-bg);
    border-bottom: 1px solid var(--color-border);
    flex-direction: column;
    padding: 12px; gap: 2px;
    max-height: calc(100vh - 56px);
    overflow-y: auto;
  }
  .site-nav.is-open { display: flex; }
  .nav-link-direct {
    width: 100%; padding: 12px 14px; font-size: 15px;
  }
  .nav-item { width: 100%; }
  .nav-trigger {
    width: 100%; justify-content: space-between;
    padding: 12px 14px; font-size: 15px;
  }
  .nav-toggle {
    display: flex; flex-direction: column; gap: 5px;
    width: 34px; height: 34px;
    align-items: center; justify-content: center;
    border-radius: var(--radius-sm);
    transition: background 0.2s;
  }
  .nav-toggle:hover { background: var(--color-bg-hover); }
  .nav-toggle span {
    display: block; width: 18px; height: 2px;
    background: var(--color-text);
    border-radius: 2px;
    transition: transform 0.25s;
  }
  .nav-toggle.is-active span:nth-child(1) { transform: translateY(3.5px) rotate(45deg); }
  .nav-toggle.is-active span:nth-child(2) { transform: translateY(-3.5px) rotate(-45deg); }
  .nav-dropdown { display: none; }
}
</style>
