<template>
  <div class="container mt-5">
    <div class="row center">
      <div class="col-md-5 mx-auto">
        <div class="card mx-auto my-5">
          <h5 class="card-header primary-color white-text text-center py-4">
            <strong>Login</strong>
          </h5>
          <div class="card-body px-lg-5 pt-0">
            <form class="text-center" style="color: #757575;" @submit.prevent="loginUser()">
              <div class="md-form">
                <input type="text" id="username" class="form-control" v-model="username" />
                <label for="username">Username</label>
              </div>
              <div class="md-form">
                <input type="password" id="password" class="form-control" v-model="password" />
                <label for="password">Password</label>
              </div>
              <button class="btn btn-primary btn-block my-4" type="submit">Login</button>
              <p>
                Not a member?
                <router-link to="/auth/register">Register</router-link>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    ...mapActions({
      login: "Auth/login"
    }),
    loginUser() {
      if (this.username !== "" && this.password !== "") {
        this.login({ username: this.username, password: this.password });
      }
    }
  }
};
</script>