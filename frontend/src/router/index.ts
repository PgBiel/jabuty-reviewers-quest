import { nextTick } from "vue";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import LoginPageView from "../views/LoginPageView.vue";
import RegisterUserView from "../views/RegisterUserView.vue";
import GameListView from "../views/GameListView.vue";
import UserProfileView from "../views/UserProfileView.vue";
import ReviewListView from "../views/ReviewListView.vue";
import TrendingGamesView from "../views/TrendingGamesView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: GameListView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginPageView,
    meta: { title: "Login" },
  },
  {
    path: "/register",
    name: "register",
    component: RegisterUserView,
    meta: { title: "Cadastro" },
  },
  {
    path: "/profile",
    name: "profile",
    component: UserProfileView,
    meta: { requiresAuth: true, title: "Perfil" },
  },
  {
    path: "/game/:id",
    name: "game",
    component: ReviewListView,
    meta: { title: "Reviews" },
  },
  {
    path: "/trending",
    name: "trending",
    component: TrendingGamesView,
    meta: { title: "Trending" },
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

const defaultTitle = "Reviewer's Quest | Jabuty";

router.afterEach((to) => {
  nextTick(() => {
    const title = to.meta != null ? to.meta.title : to.meta;
    document.title = title ? `${title} | Reviewer's Quest` : defaultTitle;
  });
});

export default router;
