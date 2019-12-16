<template>
  <div class="container">
    <div class="row my-2"></div>
    <button
      type="button"
      class="btn btn-primary mt-3"
      data-toggle="modal"
      data-target="#basicExampleModal"
      @click="newProduct()"
    >New Product</button>
    <Product
      v-for="product in products"
      :key="product.id"
      :name="product.name"
      :description="product.description"
      :price="product.price"
      :qty="product.qty"
      @delete-product="delProduct(product.id)"
      @edit-product="editProduct(product)"
    />
    <Modal v-if="showModal" />
  </div>
</template>

<script>
import { getData, postData } from "@/services/api";
import Product from "./Product/Product";
import Modal from "./Product/Modal";

export default {
  components: {
    Product,
    Modal
  },
  data() {
    return {
      products: [],
      showModal: false,
      mode: ""
    };
  },
  methods: {
    async getProducts() {
      let res = await getData("/product");
      this.products = res;
    },
    newProduct() {
      this.showModal = true;
    },
    addProduct() {},
    editProduct(product) {
      this.showModal = true;
    },
    delProduct(id) {
      console.log(id);
    }
  },
  created() {
    this.getProducts();
  }
};
</script>