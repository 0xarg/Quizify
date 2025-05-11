import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Login from "../views/Login.vue";
import Ping from "../views/Ping.vue";
import store from '@/store';
import AdminDash from '@/views/Dashboard.vue';
import SubjectList from '@/views/SubjectList.vue';
import AddSubject from '@/views/AddSubject.vue'
import SubjectDisplay from '@/views/SubjectDisplay.vue';
import ChapterList from '@/views/ChapterList.vue';
import ChapterDisplay from '@/views/ChapterDisplay.vue';
import AddChapter from '@/views/AddChapter.vue';
import SubjectChapters from '@/views/SubjectChapters.vue';
import AddQuiz from '@/views/AddQuiz.vue';
import QuizList from '@/views/QuizList.vue';
import QuizView from '@/views/QuizDisplay.vue';
import QuizDisplay from '@/views/QuizDisplay.vue';
import AddQuestion from '@/views/AddQuestion.vue';
import QuizTake from '@/views/QuizTake.vue';
import EditQuestion from '@/views/EditQuestion.vue';
import EditQuiz from '@/views/EditQuiz.vue';
import EditChapter from '@/views/EditChapter.vue';
import EditSubject from '@/views/EditSubject.vue';
import RegisterUser from '@/views/RegisterUser.vue';

const routes = [
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/",
    name: "Login",
    component: Login,

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
      role: ["admin", "user"],
    },
  },
  {
    path: "/Register",
    name: "registerUser",
    component: RegisterUser
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
    props: true,
  },
  {
    path: "/Chapters/:id",
    name: "ChapterList",
    component: ChapterList,
    props: true,
  },
  {
    path: "/AddChapter/:id",
    name: "AddChapter",
    component: AddChapter,
    props: true,
  },
  {
    path: "/EditChapter/:chapter_id",
    name: "EditChapter",
    component: EditChapter,
    props: true,
  },
  {
    path: "/Chapter/:chapter_id",
    name: "Chapter",
    component: ChapterDisplay,
    props: (route) => ({
      chapter_id: route.params.chapter_id,
      sid: route.query.subject_id,
    }),
  },
  {
    path: "/EditSubject/:subject_id",
    name: "EditSubject",
    component: EditSubject,
    props: true,
  },
  {
    path: "/AllSubjects/",
    name: "AllSubjects",
    component: SubjectChapters,
  },
  {
    path: "/AddQuiz/:chapter_id",
    name: "AddQuiz",
    component: AddQuiz,
    props: (route) => ({
      chapter_id: route.params.chapter_id,
      sid: route.query.sid,
    }),
  },

  {
    path: "/EditQuiz/:quiz_id",
    name: "EditQuiz",
    component: EditQuiz,
    props: (route) => ({
      quiz_id: route.params.quiz_id,
      cid: route.query.cid,
    }),
  },
  {
    path: "/AllSubjects/",
    name: "AllSubjects",
    component: SubjectChapters,
  },
  {
    path: "/Quizes/:chapter_id",
    name: "QuizList",
    component: QuizList,
    props: true,
  },

  {
    path: "/Quiz/:quiz_id",
    name: "Quiz",
    component: QuizDisplay,
    props: (route) => ({
      quiz_id: route.params.quiz_id,
      cid: route.query.cid,
    }),
  },
  {
    path: "/TakeQuiz/:quiz_id",
    name: "QuizTake",
    component: QuizTake,
    props: (route) => ({
      quiz_id: route.params.quiz_id,
      cid: route.query.cid,
    }),
  },
  {
    path: "/Quiz/:quiz_id/questions",
    name: "AddQuestion",
    component: AddQuestion,
    props: true,
  },
  {
    path: "/Quiz/:quiz_id/:question_id",
    name: "EditQuestion",
    component: EditQuestion,
    props: (route) => ({
      question_id: route.params.question_id,
      quiz_id: route.params.quiz_id,
    }),
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
