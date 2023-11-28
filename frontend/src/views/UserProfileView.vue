<template>
  <UserProfile />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import UserProfile from "../components/UserProfile.vue";

export default defineComponent({
  name: "UserProfile",
  components: {
    UserProfile,
  },
});
</script>
