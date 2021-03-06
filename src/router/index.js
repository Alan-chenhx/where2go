import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import PlanDetail from '../views/PlanDetail.vue'

Vue.use(VueRouter)

const routes = [{
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/login',
    name: 'login',
    // route level code-splitting
    // this generates a separate chunk (login.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import( /* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/plans',
    name: 'plans',
    // route level code-splitting
    // this generates a separate chunk (login.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import( /* webpackChunkName: "login" */ '../views/Plans.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/plan-detail',
    name: 'plan-detail',
    component: PlanDetail,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '*',
    redirect: '/'
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some(x => x.meta.requiresAuth)
  let local = JSON.parse(localStorage.getItem('vuex'));
  const session = local?local.authStatus:'';
  // console.log(session)

  if (requiresAuth && session != 'success') {
    next('/login')
  } else if (requiresAuth && session == 'success') {
    next()
  } else {
    next()
  }
})

export default router