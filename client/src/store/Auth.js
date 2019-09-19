import axios from "axios";
import router from "../router";
import jwt_decode from "jwt-decode";
import { postData } from "../services/api";

const state = {
  token: localStorage.getItem("token") || "",
  user: {},
  status: "",
  error: null,
  exp: null,
  loginTime: null
};

const getters = {
  isLoggedIn: state => {
    if (state.token == "") {
      return false;
    } else {
      if (jwt_decode(state.token).exp < parseInt(Date.now() / 1000)) {
        return false;
      } else {
        return true;
      }
    }
  },
  authState: state => state.status,
  user: state => state.user,
  error: state => state.error,
  exp: state => state.exp,
  loginTime: state => state.loginTime
};

const actions = {
  // Login Action
  async login({ commit }, user) {
    commit("auth_request");
    delete user.plainPassword;
    let res = await postData("/users/login", user);
    if (res.success) {
      let { token } = res;
      localStorage.setItem("token", token);
      axios.defaults.headers.common["Authorization"] = token;
      commit("auth_success", token);
    } else {
      commit("auth_error", res.message);
    }
  },

  // Register User
  async register({ commit }, userData) {
    commit("register_request");
    let res = await postData("/users/register", userData);
    if (res.success !== undefined) {
      commit("register_success");
      return res;
    } else {
      commit("register_error", res.message);
    }
  },

  // Get the user Profile
  async getProfile({ commit, state }) {
    let profile = await jwt_decode(state.token);
    commit("profile_loaded", profile);
  },

  // Logout the user
  async logout({ commit }, type) {
    await localStorage.removeItem("token");
    commit("logout");
    delete axios.defaults.headers.common["Authorization"];
    if (type == "none") {
      router.push("/");
    } else {
      router.push("/login");
    }
    return;
  }
};

const mutations = {
  auth_request(state) {
    state.error = null;
    state.status = "loading";
  },

  auth_success(state, token) {
    state.token = token;
    state.status = "success";
    state.error = null;
    router.push("/dashboard");
    state.loginTime = parseInt(Date.now() / 1000);
  },

  auth_error(state, message) {
    state.error = message;
  },

  register_request(state) {
    state.error = null;
    state.status = "loading";
  },

  register_success(state) {
    state.error = null;
    state.status = "success";
  },

  register_error(state, message) {
    state.error = message;
  },

  logout(state) {
    state.error = null;
    state.status = "";
    state.token = "";
    state.user = "";
  },

  profile_loaded(state, profile) {
    state.user = profile;
    state.exp = profile.exp;
  },

  user_profile(state, user) {
    state.user = user;
  }
};

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  getters
};
