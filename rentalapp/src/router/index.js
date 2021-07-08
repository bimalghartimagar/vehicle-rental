import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "../store/index.js";

Vue.use(VueRouter);

const ifNotAuthenticated = (to, from, next) => {
  if (!store.getters.isAuthenticated) {
    next();
    return;
  }
  next("/");
};

const ifAuthenticated = (to, from, next) => {
  if (store.getters.isAuthenticated) {
    next();
    return;
  }
  next("/login");
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Login.vue"),
    beforeEnter: ifNotAuthenticated,
  },
  {
    path: "/signup",
    name: "Signup",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Signup.vue"),
    beforeEnter: ifNotAuthenticated,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () =>
      import(/* webpackChunkName: "dashboard" */ "../views/Dashboard.vue"),
    beforeEnter: ifAuthenticated,
    children: [
      {
        path: "rentals",
        name: "Rentals",
        component: () =>
          import(
            /* webpackChunkName: "rentals" */ "@/components/dashboard/Rentals.vue"
          ),
        beforeEnter: ifAuthenticated,
      },
      {
        path: "vehicles",
        name: "Vehicles",
        component: () =>
          import(
            /* webpackChunkName: "vehicles" */ "@/components/dashboard/Vehicles.vue"
          ),
        beforeEnter: ifAuthenticated,
      },
      {
        path: "vendors",
        name: "vendors",
        component: () =>
          import(
            /* webpackChunkName: "vendors" */ "@/components/dashboard/Vendors.vue"
          ),
        beforeEnter: ifAuthenticated,
      },
      {
        path: "usertypes",
        name: "UserTypes",
        component: () =>
          import(
            /* webpackChunkName: "usertypes" */ "@/components/dashboard/UserTypes.vue"
          ),
        beforeEnter: ifAuthenticated,
      },
    ],
  },
  {
    path: "/search",
    name: "Search",
    component: () =>
      import(/* webpackChunkName: "search" */ "../views/Search.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
