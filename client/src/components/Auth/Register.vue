<template>
  <div class="container mt-5">
    <div class="row center">
      <div class="col-md-5 mx-auto">
        <div class="card mx-auto">
          <h5 class="card-header primary-color white-text text-center py-4">
            <strong>Register</strong>
          </h5>
          <div class="card-body px-lg-5 pt-0">
            <form class="text-center" style="color: #757575;">
              <div class="md-form">
                <input type="text" id="username" class="form-control" v-model="user.username" />
                <label for="username">Username</label>
              </div>
              <div class="md-form">
                <input type="text" id="name" class="form-control" v-model="user.name" />
                <label for="name">Name</label>
              </div>
              <div class="md-form">
                <input type="email" id="email" class="form-control" v-model="user.email" />
                <label for="email">E-mail</label>
              </div>
              <div class="md-form">
                <input
                  type="password"
                  id="password"
                  class="form-control validate"
                  v-model="user.password"
                />
                <label
                  for="password"
                  :data-error="passwordError ? passwordError : null"
                  :data-success="!passwordError ? 'Password matched' : null"
                >Password</label>
              </div>
              <div class="md-form">
                <input
                  type="password"
                  id="confirmpassword"
                  class="form-control validate"
                  v-model="user.confirmPassword"
                />
                <label
                  for="confirmpassword"
                  :data-error="passwordError ? passwordError : null"
                  :data-success="!passwordError ? 'Password matched' : null"
                >Confirm Password</label>
              </div>
              <button class="btn btn-primary btn-block my-4" type="submit">Register</button>
              <p>
                Already a member?
                <router-link to="/auth/login">Login</router-link>
              </p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { postData } from "@/services/api";
import { mapActions } from "vuex";

export default {
  data() {
    return {
      user: {
        name: "",
        username: "",
        password: "",
        confirmPassword: ""
      }
    };
  },
  computed: {
    passwordError() {
      return this.user.password !== this.user.confirmPassword &&
        this.user.password &&
        this.user.confirmPassword
        ? "Passwords don't match"
        : null;
    }
  },
  methods: {}
};
</script>