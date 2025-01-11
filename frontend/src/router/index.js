import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login.vue";
import Ping from "../views/Ping.vue";
import store from '@/store';
import AdminDash from '@/views/Admin-Dash.vue';
import SubjectList from '@/views/SubjectList.vue';

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    meta :{
      requiresLogin: true
    }
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ "../views/AboutView.vue");
    },
  },
  {
    path: "/dashboard",
    name: "dash",
    component: AdminDash,
    meta: {
      requiresLogin: true,
      role: "admin" },
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/ping",
    name: "ping",
    component: Ping,
  },
  {
    path: "/subjects",
    name: "SubjectList",
    component: SubjectList,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next) => {
  if (to.matched.some((record)=>record.meta.requiresLogin)) {
    if (!store.state.loggedIn){
      next ({path: '/login'});
    } else if(to.meta.role && (to.meta.role != store.state.roles)) {
      alert("Only Authorized Users has Access to this Page. Redirecting to Home.....")
      next({path:'/'})
    } else {
      next();
    }
  }
  else{
    next();
  }
  
})
export default router
