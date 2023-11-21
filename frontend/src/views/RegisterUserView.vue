<template>
  <RegisterUser />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import RegisterUser from "../components/RegisterUser.vue";

export default defineComponent({
  name: "RegisterView",
  components: {
    RegisterUser,
  },
});
</script>
