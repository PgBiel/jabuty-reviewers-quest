<template>
  <NavBar />
  <GameList is-trending />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import GameList from "../components/GameList.vue";
import NavBar from "../components/NavBar.vue";

export default defineComponent({
  name: "TrendingGamesView",
  components: {
    GameList,
    NavBar,
  },
});
</script>
