import { createRouter, createWebHistory } from "vue-router";
import UserLogin from "@/components/user/UserLogin.vue";
import UserSignUp from "@/components/user/UserSignUp.vue";
import MainPage from "@/components/MainPage.vue";

const routes = [
  {
    path : "/",
    component: MainPage
  },
  {
    path : "/user-login",
    component: UserLogin
  },
  {
    path: "/user-signup",
    component: UserSignUp
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
