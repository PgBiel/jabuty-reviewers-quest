<template>
  <div>
    <h1>Register User</h1>
    <RegisterUser />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import RegisterUser from "./RegisterUser.vue";

export default defineComponent({
  name: "RegisterView",
  components: {
    RegisterUser,
  },
});
</script>
