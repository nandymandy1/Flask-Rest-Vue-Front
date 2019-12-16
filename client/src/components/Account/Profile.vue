<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 mt-5">
        <div class="card" v-if="Object.keys(user).length">
          <div class="card-body">
            <h4 class="card-title">
              <a>{{ user.username }}</a>
            </h4>
            <p class="card-text">{{user.email}}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
  computed: {
    ...mapGetters({
      user: "Auth/user"
    })
  },

  methods: {
    ...mapActions({
      getProfile: "Auth/getProfile"
    })
  },
  created() {
    this.getProfile();
  }
};
</script>