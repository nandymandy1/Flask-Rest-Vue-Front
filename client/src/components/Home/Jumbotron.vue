<template>
  <div class="jumbotron card card-image">
    <div class="text-white text-center py-5 px-4">
      <div>
        <h2 class="card-title h1-responsive pt-3 mb-5 font-bold">
          <strong>SIMPLE VUE-FLASK APPLICATION</strong>
        </h2>
        <p
          class="mx-5 mb-5"
        >Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nihil voluptatum dolorum, eum praesentium minima tenetur pariatur doloribus quod rem animi..</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      backgroundUrl: `url(${require("@/assets/theme.jpeg")})`
    };
  }
};
</script>

<style scoped>
.card-image {
  background-image: linear-gradient(
    to right,
    #002f87,
    #0068c2,
    #009bd0,
    #00cbb1,
    #45f47a
  );
}
</style>