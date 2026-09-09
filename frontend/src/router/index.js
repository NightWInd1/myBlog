import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import TechNotes from '../pages/TechNotes.vue'
import LifeNotes from '../pages/LifeNotes.vue'
import CategoryPage from '../pages/CategoryPage.vue'
import About from '../pages/About.vue'
import PostDetail from '../pages/PostDetail.vue'
import SearchResults from '../pages/SearchResults.vue'

const routes = [
  { path: '/', name: 'Home', component: Home },
  { path: '/category/tech', name: 'TechNotes', component: TechNotes },
  { path: '/category/life', name: 'LifeNotes', component: LifeNotes },
  { path: '/category/:slug', name: 'CategoryPage', component: CategoryPage },
  { path: '/about', name: 'About', component: About },
  { path: '/post/:slug', name: 'PostDetail', component: PostDetail },
  { path: '/search', name: 'SearchResults', component: SearchResults },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
