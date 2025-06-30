import { createRouter, createWebHistory } from 'vue-router'
import Login from "../views/Login.vue";
import store from '@/store';
import AdminDash from '@/views/Dashboard.vue';
import SubjectList from '@/views/SubjectList.vue';
import ChapterList from '@/views/ChapterList.vue';
import QuizList from '@/views/QuizList.vue';
import QuizTake from '@/views/QuizTake.vue';
import RegisterUser from '@/views/RegisterUser.vue';
import AdminQuiz from '@/views/AdminQuiz.vue';

const routes = [
  {
    path: "/",
    name: "Login",
    component: Login,
  },

  {
    path: "/dashboard",
    name: "dash",
    component: AdminDash,
    meta: {
      requiresLogin: true,
      role: ["admin", "user"],
    },
  },
  {
    path: "/Register",
    name: "registerUser",
    component: RegisterUser,
  },

  {
    path: "/subjects",
    name: "SubjectList",
    component: SubjectList,
    meta: {
      requiresLogin: true,
      role: ["admin", "user"],
    },
  },

  {
    path: "/Chapters/:subject_id",
    name: "ChapterList",
    component: ChapterList,
    props: (route) => ({
      sid: route.params.subject_id,
      sname: route.query.subject_name,
      tchapters: route.query.totalChapters,
    }),
    meta: {
      requiresLogin: true,
      role: ["admin", "user"],
    },
  },

  {
    path: "/Quizes/:chapter_id",
    name: "QuizList",
    component: QuizList,
    props: (route) => ({
      cid: route.params.chapter_id,
      cname: route.query.chapter_name,
      tquiz: route.query.totalQuiz,
    }),
    meta: {
      requiresLogin: true,
      role: ["admin", "user"],
    },
  },

  {
    path: "/Quiz/:quiz_id",
    name: "Quiz",
    component: AdminQuiz,
    props: (route) => ({
      quiz_id: route.params.quiz_id,
      remarks: route.query.remarks,
      tques: route.query.totalQues,
      cid: route.query.chapter_id,
      cname: route.query.chapter_name,
    }),
    meta: {
      requiresLogin: true,
      role: ["admin"],
    },
  },
  {
    path: "/TakeQuiz/:quiz_id",
    name: "QuizTake",
    component: QuizTake,
    props: (route) => ({
      quiz_id: route.params.quiz_id,
      cid: route.query.chapter_id,
    }),
    meta: {
      requiresLogin: true,
      role: ["user"],
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to,from,next) => {
  if (to.matched.some((record)=>record.meta.requiresLogin)) {
    if (!store.state.loggedIn){
      next ({path: '/'});
    } else if (
      to.meta.role &&
      !to.meta.role.some((role) => store.state.roles.includes(role))
    ) {
      alert(
        "Only Authorized Users has Access to this Page. Redirecting to Home....."
      );
      next({ path: "/" });
    } else {
      next();
    }
  }
  else{
    next();
  }
  
})
export default router
