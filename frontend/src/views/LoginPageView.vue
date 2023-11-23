<template>
  <LoginUser />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import LoginUser from "../components/LoginUser.vue";

export default defineComponent({
  name: "LoginView",
  components: {
    LoginUser,
  },
});
</script>
