<template>
  <NavBar />
  <TrendingGames />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import TrendingGames from "../components/TrendingGames.vue";
import NavBar from "../components/NavBar.vue";

export default defineComponent({
  name: "TrendingGamesView",
  components: {
    TrendingGames,
    NavBar,
  },
});
</script>
