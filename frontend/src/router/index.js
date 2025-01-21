import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login.vue";
import Ping from "../views/Ping.vue";
import store from '@/store';
import AdminDash from '@/views/Admin-Dash.vue';
import SubjectList from '@/views/SubjectList.vue';
import AddSubject from '@/views/AddSubject.vue'
import SubjectDisplay from '@/views/SubjectDisplay.vue';
import ChapterList from '@/views/ChapterList.vue';
import ChapterDisplay from '@/views/ChapterDisplay.vue';
import AddChapter from '@/views/AddChapter.vue';
import SubjectChapters from '@/views/SubjectChapters.vue';

const routes = [
  {
    path: "/",
    name: "home",
    component: Home,
    meta: {
      requiresLogin: true,
    },
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
      role: "admin",
    },
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
  {
    path: "/add-subjects",
    name: "AddSubject",
    component: AddSubject,
  },
  {
    path: "/Subject/:id",
    name: "SubjectDisplay",
    component: SubjectDisplay,
    props: true
  },
  {
    path: "/Chapters/:id",
    name: "ChapterList",
    component: ChapterList,
    props: true
  },
  {
    path: "/AddChapter/:id",
    name: "AddChapter",
    component: AddChapter,
    props: true
  },
  {
    path: "/Chapter/:chapter_id",
    name: "Chapter",
    component: ChapterDisplay,
    props: (route) =>({
      chapter_id: route.params.chapter_id,
      subject_id: route.query.subject_id
    })
  },
  {
    path: "/AllSubjects/",
    name: "AllSubjects",
    component: SubjectChapters,
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
