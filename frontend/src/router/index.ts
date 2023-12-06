import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import LoginPageView from "../views/LoginPageView.vue";
import RegisterUserView from "../views/RegisterUserView.vue";
import GameListView from "../views/GameListView.vue";
import UserProfileView from "../views/UserProfileView.vue";
import ReviewListView from "../views/ReviewListView.vue";

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
    path: "/login",
    name: "login",
    component: LoginPageView,
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
  {
    path: "/profile",
    name: "profile",
    component: UserProfileView,
    meta: { requiresAuth: true },
  },
  {
    path: "/game/:id",
    name: "game",
    component: ReviewListView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  if (to.meta != null && "requiresAuth" in to.meta && to.meta.requiresAuth) {
    fetch("/api/user/self")
      .then((response) => {
        if (response.ok) {
          // user logged-in, proceed
          next();
        } else {
          // user not logged-in, please log in
          next({ name: "login" });
        }
      })
      .catch((error) => {
        console.error("Couldn't verify user authentication:", error);
      });
  } else {
    next();
  }
});

export default router;
