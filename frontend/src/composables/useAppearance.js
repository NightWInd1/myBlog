import { ref, watch } from 'vue'
import { readPreference, savePreference } from '../utils/format'
import { site } from '../config/site'
const theme = ref(readPreference('blog-theme', 'light'))
const hue = ref(Number(readPreference('blog-hue', String(site.defaultHue))))
const layout = ref(readPreference('blog-layout', 'list'))
if (!['light', 'dark', 'system'].includes(theme.value)) theme.value = 'light'
if (!['list', 'grid'].includes(layout.value)) layout.value = 'list'
if (!Number.isFinite(hue.value) || hue.value < 0 || hue.value > 360)
  hue.value = site.defaultHue
const media = window.matchMedia('(prefers-color-scheme: dark)')
const resolvedTheme = ref('light')
function apply() {
  resolvedTheme.value =
    theme.value === 'system' ? (media.matches ? 'dark' : 'light') : theme.value
  document.documentElement.dataset.theme = resolvedTheme.value
  document.documentElement.style.setProperty('--hue', hue.value)
}
media.addEventListener('change', apply)
watch(
  [theme, hue, layout],
  () => {
    apply()
    savePreference('blog-theme', theme.value)
    savePreference('blog-hue', String(hue.value))
    savePreference('blog-layout', layout.value)
  },
  { immediate: true },
)
export function useAppearance() {
  return { theme, resolvedTheme, hue, layout }
}
