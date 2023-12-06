<template>
  <NavBar />
  <UserProfile />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import UserProfile from "../components/UserProfile.vue";
import NavBar from "../components/NavBar.vue";

export default defineComponent({
  name: "UserProfileView",
  components: {
    UserProfile,
    NavBar,
  },
});
</script>
