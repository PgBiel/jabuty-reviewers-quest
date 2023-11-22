<template>
  <NavBar />
  <GameList />
</template>

<script lang="ts">
import { defineComponent } from "vue";

// Components
import GameList from "../components/GameList.vue";
import NavBar from "../components/NavBar.vue";

export default defineComponent({
  name: "GameListView",
  components: {
    GameList,
    NavBar,
  },
});
</script>
