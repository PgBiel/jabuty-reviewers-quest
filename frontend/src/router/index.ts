import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import RegisterUserView from "../views/RegisterUserView.vue";
import GameListView from "../views/GameListView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: GameListView,
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
