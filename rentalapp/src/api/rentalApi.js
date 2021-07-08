import axios from "axios";
import localstorageservice from "../utils/localstorage";
import store from "../store/index.js";

const localStorageService = localstorageservice.getService();

axios.interceptors.request.use(
  (config) => {
    let token = localStorageService.getAccessToken();

    if (
      config.url.indexOf("logout2") > -1 ||
      config.url.indexOf("refresh") > -1
    ) {
      token = localStorageService.getRefreshToken();
    }

    if (token) {
      config.headers["Authorization"] = "Bearer " + token;
    }
    config.headers["Content-Type"] = "application/json";
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

function createResponseInterceptor() {
  const responseInterceptor = axios.interceptors.response.use(
    (response) => {
      return response;
    },
    (error) => {
      const originalRequest = error.config;
      if (
        error.response.status === 401 &&
        error.response.data.msg === "Token has expired"
      ) {
        axios.interceptors.response.eject(responseInterceptor);
        return axios
          .post("auth/refresh/")
          .then((response) => {
            if (response.status === 200) {
              localStorageService.refreshToken(response.data);
              store.dispatch("refresh_token", response.data);
              return axios(originalRequest);
            }
          })
          .catch((error) => {
            console.log(error);
          })
          .finally(createResponseInterceptor());
      } else if (
        error.response.status === 401 &&
        (error.response.data.msg === "User not authorized" ||
          error.response.data.msg === "Missing Authorization Header")
      ) {
        store.dispatch("unauth");
      }
      return Promise.reject(error);
    }
  );
}

createResponseInterceptor();

axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;

export default axios;
