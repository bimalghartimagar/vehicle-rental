import Vue from "vue";
import Vuex from "vuex";
import rentalApi from "@/api/rentalApi";
import localstorage from "../utils/localstorage.js";
import router from "../router"
const localStorageService = localstorage.getService();

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    access_token: localStorageService.getAccessToken() || "",
    refresh_token: localStorageService.getRefreshToken() || ""
  },
  mutations: {
    login_success: (state, obj) => {
      state.access_token = obj.access_token;
      state.refresh_token = obj.refresh_token;
    },
    logout_success: state => {
      state.access_token = "";
      state.refresh_token = "";
    },
    refresh_token: (state, obj) => {
      state.access_token = obj.access_token;
    }
  },
  actions: {
    login: ({ commit }, user) => {
      return rentalApi
        .post("auth/login/", {
          username: user.username,
          password: user.password
        })
        .then(response => {
          localStorageService.setToken(response.data);
          commit("login_success", response.data);
          return Promise.resolve(user);
        })
        .catch(error => {
          return Promise.reject(error);
        });
    },
    logout: ({ commit }) => {
      return rentalApi
        .all([
          rentalApi.delete("auth/logout/"),
          rentalApi.delete("auth/logout2/")
        ])
        .then(() => {
          localStorageService.clearToken();
          commit("logout_success");
          return Promise.resolve();
        })
        .catch(error => {
          if (error.response.status === 401) {
            localStorageService.clearToken();
            commit("logout_success");
          }
          return Promise.reject(error);
        });
    },
    unauth: ({ commit }) => {
      localStorageService.clearToken();
      commit("logout_success");
      router.push('/')
    }
  },
  modules: {},
  getters: {
    isAuthenticated: state => !!state.access_token && !!state.refresh_token,
    getRefreshToken: state => state.refresh_token
  }
});
