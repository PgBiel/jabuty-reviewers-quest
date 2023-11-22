import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegisterUserView from "../views/RegisterUserView.vue";
<<<<<<< HEAD
import GameListView from "../views/GameListView.vue";
=======
import LoginPageView from '../views/LoginPageView.vue';
>>>>>>> 0966930 (Login front)

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: RegisterUserView,
  },
  {
    path: "/gamelist",
    name: "gamelist",
    component: GameListView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
