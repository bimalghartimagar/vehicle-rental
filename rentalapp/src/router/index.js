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
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
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
    path: "/contactus",
    name: "CcontactUs",
    component: () =>
      import(/* webpackChunkName: "contactus" */ "../views/ContactUs.vue")
  },
  {
    path: "/vehicles",
    name: "Vehicles",
    component: () =>
      import(/* webpackChunkName: "vehicles" */ "../views/Vehicles.vue"),
    beforeEnter: ifAuthenticated
  },
  {
    path: "/vendors",
    name: "vendors",
    component: () =>
      import(/* webpackChunkName: "vendors" */ "../views/Vendors.vue"),
    beforeEnter: ifAuthenticated
  },
  {
    path: "/usertypes",
    name: "UserTypes",
    component: () =>
      import(/* webpackChunkName: "usertypes" */ "../views/UserTypes.vue"),
    beforeEnter: ifAuthenticated
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
