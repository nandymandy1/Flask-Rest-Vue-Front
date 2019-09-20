<template>
  <div class="card">
    <img class="card-img-top" :src="imageURL" height="300" width="300" alt="Card image cap" />
    <div class="card-body">
      <h4 class="card-title">
        <a>{{ title }}</a>
      </h4>
      <p class="card-text">{{ text }}</p>
      <a v-if="buttonLink" :href="buttonLink" target="_blank" class="btn btn-primary">Learn More</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: String,
    text: String,
    imageURL: String,
    buttonLink: String
  }
};
</script>