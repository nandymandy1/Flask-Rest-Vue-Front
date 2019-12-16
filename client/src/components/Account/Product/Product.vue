<template>
  <div class="card mt-2">
    <div class="card-body">
      <div class="row">
        <div class="col-md-9">
          <h5 class="card-title">{{ name }}</h5>
          <p class="card-text">{{ description }}</p>
        </div>
        <div class="col-md-3">
          <h6 class="ml-auto">Quantity: {{ qty }}</h6>
          <h6 class="ml-auto">Price: {{ price }}/-</h6>
        </div>
      </div>
      <button class="btn btn-danger btn-sm" @click="$emit('delete-product')">Remove</button>
      <button class="btn btn-info btn-sm" @click="$emit('edit-product')">Edit</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    description: String,
    id: Number,
    name: String,
    price: Number,
    qty: Number
  }
};
</script>