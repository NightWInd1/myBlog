import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'Home', component: Home, meta: { title: '首页' } },
    {
      path: '/category/:slug',
      name: 'CategoryPage',
      component: () => import('../pages/CategoryPage.vue'),
      meta: { title: '文章分类' },
    },
    {
      path: '/categories',
      name: 'Categories',
      component: () => import('../pages/Categories.vue'),
      meta: { title: '所有分类' },
    },
    {
      path: '/archives',
      name: 'Archives',
      component: () => import('../pages/Archives.vue'),
      meta: { title: '文章归档' },
    },
    {
      path: '/about',
      name: 'About',
      component: () => import('../pages/About.vue'),
      meta: { title: '关于晚风' },
    },
    {
      path: '/post/:slug',
      name: 'PostDetail',
      component: () => import('../pages/PostDetail.vue'),
      meta: { title: '文章' },
    },
    {
      path: '/search',
      name: 'SearchResults',
      component: () => import('../pages/SearchResults.vue'),
      meta: { title: '搜索' },
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      component: () => import('../pages/NotFound.vue'),
      meta: { title: '页面未找到' },
    },
  ],
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    if (to.hash) return { el: to.hash, top: 92 }
    return { top: 0 }
  },
})
router.afterEach((to) => {
  document.title = `${to.meta.title} · 晚风如歌`
})
export default router
