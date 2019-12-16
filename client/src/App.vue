<template>
  <div id="app">
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
<style scoped>
</style>
