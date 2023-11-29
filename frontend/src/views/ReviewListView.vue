<template>
  <NavBar />
  <ReviewList />
</template>

<script lang="ts">
import { defineComponent } from "vue";

import ReviewList from "../components/ReviewList.vue";
import NavBar from "../components/NavBar.vue";

export default defineComponent({
  name: "ReviewListView",
  components: {
    ReviewList,
    NavBar,
  },
});
</script>
