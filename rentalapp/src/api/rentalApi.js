import axios from "axios";
import localstorageservice from "../utils/localstorage";
const localStorageService = localstorageservice.getService();

axios.interceptors.request.use(
  config => {
    const token = localStorageService.getAccessToken();

    if (token) {
      config.headers["Authorization"] = "Bearer " + token;
    }
    config.headers["Content-Type"] = "application/json";
    return config;
  },
  error => {
    Promise.reject(error);
  }
);

axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;

export default axios;
