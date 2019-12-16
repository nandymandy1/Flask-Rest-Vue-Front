<template>
  <div class="mb-5">
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top my-primary-gradient">
      <a class="navbar-brand" href="/">
        <b>Vue-Flask</b>
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#basicExampleNav"
        aria-controls="basicExampleNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="basicExampleNav">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about">About</router-link>
          </li>
        </ul>

        <ul class="navbar-nav ml-auto mr-4">
          <li class="nav-item" v-if="!loggedIn">
            <router-link class="nav-link" to="/auth/login">Login</router-link>
          </li>
          <li class="nav-item" v-if="!loggedIn">
            <router-link class="nav-link" to="/auth/register">Register</router-link>
          </li>
          <li class="nav-item" v-if="loggedIn">
            <router-link class="nav-link" to="/accounts/products">Products</router-link>
          </li>
          <li class="nav-item dropdown" v-if="loggedIn">
            <a
              class="nav-link dropdown-toggle"
              id="navbarDropdownMenuLink"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >Accounts</a>
            <div class="dropdown-menu dropdown-primary" aria-labelledby="navbarDropdownMenuLink">
              <router-link to="/accounts/profile" class="dropdown-item">Profile</router-link>
              <a class="dropdown-item" href="#" @click.prevent="logoutUser()">Logout</a>
            </div>
          </li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  computed: {
    ...mapGetters({
      loggedIn: "Auth/isLoggedIn"
    })
  },
  methods: {
    ...mapActions({
      logoutUser: "Auth/logout"
    })
  }
};
</script>

<style scoped>
.my-primary-gradient {
  background: linear-gradient(
    to right,
    #002f87,
    #0068c2,
    #009bd0,
    #00cbb1,
    #45f47a
  );
}
</style>