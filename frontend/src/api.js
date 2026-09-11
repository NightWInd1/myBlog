export async function get(url, options = {}) {
  const res = await fetch(url, options)
  if (!res.ok) {
    const error = new Error(
      res.status === 404 ? '内容不存在或已被移走' : '暂时无法加载，请稍后重试',
    )
    error.status = res.status
    throw error
  }
  return res.json()
}
export const fetchPosts = (page = 1, params = {}, options) =>
  get(`/api/posts/?${new URLSearchParams({ page, ...params })}`, options)
export const fetchPinnedPosts = () => get('/api/posts/pinned/')
export const fetchLatestPosts = () => get('/api/posts/latest/')
export const fetchPostBySlug = (slug, options) =>
  get(`/api/posts/${encodeURIComponent(slug)}/`, options)
export const fetchLatestComments = () => get('/api/comments/latest/')
export const searchPosts = (q, page = 1, options) =>
  get(`/api/posts/search/?${new URLSearchParams({ q, page })}`, options)
export default { get }
