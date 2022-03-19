import {
  createRouter,
  createWebHistory,
  RouteRecordRaw
} from 'vue-router';
import Home from '../views/home.vue';
import Contact from '../views/contact.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact
  },
]

const router = createRouter({
  history: createWebHistory((import.meta.env.VITE_BASE_URL === undefined || import.meta.env.VITE_BASE_URL === false || import.meta.env.VITE_BASE_URL === true) ? '/' : import.meta.env.VITE_BASE_URL),
  routes
})

router.beforeEach( (to, from, next) => {
  next();
})

export default router