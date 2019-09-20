<template>
  <div class="home">
    <Jumbotron />
    <div class="container">
      <div class="row">
        <div class="col-md-4" v-for="card in cardData" :key="card.title">
          <Card
            :title="card.title"
            :imageURL="card.imageURL"
            :text="card.text"
            :buttonLink="card.buttonLink"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Card from "@/components/Utils/Card.vue";
import Jumbotron from "@/components/Home/Jumbotron.vue";

export default {
  components: {
    Jumbotron,
    Card
  },
  data() {
    return {
      cardData: [
        {
          title: "Flask Framework",
          text:
            "Flask framework is widly used to build the rest services. Its a python microfamework framework.",
          imageURL: require("../assets/flask.png"),
          buttonLink: "https://www.fullstackpython.com/flask.html"
        },
        {
          title: "Vue.js Library",
          text:
            "Vue.js is a simplest and minimilistic javascript library, widely used for the client app.",
          imageURL: require("../assets/vue.png"),
          buttonLink: "https://vuejs.org/"
        },
        {
          title: "Python Javascript",
          text:
            "We have tapped the real power of Vue.js and Python by creating rest service with Python and App by Vue.js",
          imageURL: "https://miro.medium.com/max/960/0*AdLUN2sms12Y8AVo.jpg",
          buttonLink:
            "https://codeburst.io/full-stack-single-page-application-with-vue-js-and-flask-b1e036315532"
        }
      ]
    };
  }
};
</script>

<style scoped>
</style>
