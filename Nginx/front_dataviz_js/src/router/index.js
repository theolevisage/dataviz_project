import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import ChartI from '../views/ChartI.vue'
import ChartII from '../views/ChartII.vue'
import ChartIII from '../views/ChartIII.vue'
import ChartIV from '../views/ChartIV.vue'
import ChartV from '../views/ChartV.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/ChartI',
    name: 'ChartI',
    component: ChartI
  },
  {
    path: '/ChartII',
    name: 'ChartII',
    component: ChartII
  },
  {
    path: '/ChartIII',
    name: 'ChartIII',
    component: ChartIII
  },
  {
    path: '/ChartIV',
    name: 'ChartIV',
    component: ChartIV
  },
  {
    path: '/ChartV',
    name: 'ChartV',
    component: ChartV
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
