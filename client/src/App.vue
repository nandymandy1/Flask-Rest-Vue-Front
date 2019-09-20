<template>
  <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div>-->
    <Navbar />
    <router-view />
  </div>
</template>
<script>
import Navbar from "@/components/Layout/Navbar.vue";
export default {
  components: {
    Navbar
  }
};
</script>
<style>
</style>
