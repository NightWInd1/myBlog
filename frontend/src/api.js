const BASE = '/api'

export async function fetchPosts(page = 1, params = {}) {
  const query = new URLSearchParams({ page, ...params }).toString()
  const res = await fetch(`${BASE}/posts/?${query}`)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function fetchPinnedPosts() {
  const res = await fetch(`${BASE}/posts/pinned/`)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function fetchLatestPosts() {
  const res = await fetch(`${BASE}/posts/latest/`)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function fetchPostBySlug(slug) {
  const res = await fetch(`${BASE}/posts/${slug}/`)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function fetchLatestComments() {
  const res = await fetch(`${BASE}/comments/latest/`)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function searchPosts(q, page = 1) {
  const query = new URLSearchParams({ q, page }).toString()
  const res = await fetch(`${BASE}/posts/search/?${query}`)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export async function get(url) {
  const res = await fetch(url)
  if (!res.ok) throw new Error(`API error: ${res.status}`)
  return res.json()
}

export default { get }
