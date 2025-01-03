// import Vue from "vue";
// import VueRouter from "vue-router";
// import Login from "../pages/Login.vue";

// Vue.use(VueRouter);

// const routes = [{ path: "/login", component: Login }];

// const router = new VueRouter({
//   routes,
// });

// export default router;


// import { createRouter, createWebHistory } from "vue-router";
// import Login from "../pages/Login.vue";

// const routes = [{ path: "/login", name: 'Login', component: Login }];

// const router = createRouter({
//   history: createWebHistory(), // Use history mode
//   routes,
// });

// export default router;

import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Ping from '../views/Ping.vue'

const routes = [
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
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

console.log("Routes:", routes);
export default router