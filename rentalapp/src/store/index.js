import Vue from "vue";
import Vuex from "vuex";
import rentalApi from "../api/rentalApi";
import localstorage from "../utils/localstorage.js";
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
      rentalApi
        .post("auth/login/", {
          username: user.username,
          password: user.password
        })
        .then(response => {
          localStorageService.setToken(response.data);
          commit("login_success", response.data);
          Promise.resolve(user);
        })
        .catch(error => {
          Promise.reject(error);
        });
    },
    logout: ({ commit }) => {
      rentalApi
        .all([
          rentalApi.delete("auth/logout/"),
          rentalApi.delete("auth/logout2/")
        ])
        .then(() => {
          localStorageService.clearToken();
          commit("logout_success");
        })
        .catch(error => {
          if (error.response.status === 401) {
            localStorageService.clearToken();
            commit("logout_success");
          }
        });
    }
  },
  modules: {},
  getters: {
    isAuthenticated: state => !!state.access_token,
    getRefreshToken: state => state.refresh_token
  }
});
