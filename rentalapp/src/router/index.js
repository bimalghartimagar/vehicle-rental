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
    component: Home
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Login.vue"),
    beforeEnter: ifNotAuthenticated
  },
  {
    path: "/signup",
    name: "Signup",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Signup.vue"),
    beforeEnter: ifNotAuthenticated
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: () =>
      import(/* webpackChunkName: "dashboard" */ "../views/Dashboard.vue"),
    beforeEnter: ifAuthenticated,
    children: [
      {
        path: "vehicles",
        name: "Vehicles",
        component: () =>
          import(
            /* webpackChunkName: "vehicles" */ "../components/Vehicles.vue"
          )
        // beforeEnter: ifAuthenticated
      },
      {
        path: "vendors",
        name: "vendors",
        component: () =>
          import(/* webpackChunkName: "vendors" */ "../components/Vendors.vue")
        // beforeEnter: ifAuthenticated
      },
      {
        path: "usertypes",
        name: "UserTypes",
        component: () =>
          import(
            /* webpackChunkName: "usertypes" */ "../components/UserTypes.vue"
          )
        // beforeEnter: ifAuthenticated
      }
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
