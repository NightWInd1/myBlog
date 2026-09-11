import { computed, ref } from 'vue'
import { get } from '../api'
import { flattenCategories } from '../utils/format'

const categories = ref([])
const stats = ref(null)
const comments = ref([])
const latest = ref([])
const loading = ref(false)
const error = ref(false)
let pending
export function useSite() {
  async function load() {
    if (pending) return pending
    loading.value = true
    pending = Promise.allSettled([
      get('/api/categories/'),
      get('/api/stats/'),
      get('/api/comments/latest/'),
      get('/api/posts/latest/'),
    ])
      .then((results) => {
        const targets = [categories, stats, comments, latest]
        results.forEach((result, i) => {
          if (result.status === 'fulfilled') targets[i].value = result.value
        })
        error.value = results.some((result) => result.status === 'rejected')
      })
      .finally(() => {
        loading.value = false
        pending = null
      })
    return pending
  }
  return {
    categories,
    flatCategories: computed(() => flattenCategories(categories.value)),
    stats,
    comments,
    latest,
    loading,
    error,
    load,
  }
}
