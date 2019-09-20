import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

// Views
import Auth from "@/views/Auth.vue";
import Accounts from "@/views/Accounts.vue";
import Home from "./views/Home.vue";
/**
 * Components
 */
// Public Components
import Register from "@/components/Auth/Register.vue";
import Login from "@/components/Auth/Login.vue";
// Authenticated Components
import Products from "@/components/Account/Products.vue";
import Profile from "@/components/Account/Profile.vue";

let AuthRoutes = {
  path: "/auth",
  component: Auth,
  name: "Auth",
  redirect: "/auth/login",
  meta: {
    requiresAuth: false
  },
  children: [
    {
      path: "login",
      name: "AuthLogin",
      component: Login
    },
    {
      path: "register",
      name: "AuthRegister",
      component: Register
    }
  ]
};

let AccountRoutes = {
  path: "/accounts",
  component: Accounts,
  name: "Accounts",
  redirect: "/accounts",
  meta: {
    requiresAuth: true
  },
  children: [
    {
      path: "products",
      name: "Products",
      component: Products
    },
    {
      path: "profile",
      name: "Profile",
      component: Profile
    }
  ]
};

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/about",
      name: "about",
      component: () => import("./views/About.vue")
    },
    AuthRoutes,
    AccountRoutes
  ]
});
