export function formatDate(value) {
  if (!value) return '—'
  return new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  })
    .format(new Date(value))
    .replaceAll('/', '-')
}
export function flattenCategories(items, depth = 0) {
  return items.flatMap((item) => [
    { ...item, depth },
    ...flattenCategories(item.children || [], depth + 1),
  ])
}
export function readPreference(key, fallback) {
  try {
    return localStorage.getItem(key) || fallback
  } catch {
    return fallback
  }
}
export function savePreference(key, value) {
  try {
    localStorage.setItem(key, value)
  } catch {
    /* Private browsing can disable storage. */
  }
}
