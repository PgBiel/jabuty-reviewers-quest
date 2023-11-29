<template>
  <v-app-bar app>
    <v-container>
      <v-row align="center">
        <v-col cols="auto" lg="3">
          <v-btn>Reviews</v-btn>
        </v-col>
        <v-col cols="auto" lg="3">
          <v-btn>Recommended</v-btn>
        </v-col>
        <v-col cols="auto" lg="3">
          <v-btn>Trending</v-btn>
        </v-col>
        <v-col cols="3" lg="2" class="ml-auto">
          <v-combobox
            v-model="search"
            :items="games"
            item-title="name"
            item-value="game_id"
            label="Search"
            hide-details
            clearable
            @input="searchGames"
            @update:modelValue="gameSelected"
          ></v-combobox>
        </v-col>
        <v-col cols="auto" class="ml-auto">
          <v-icon>mdi-account-circle</v-icon>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script lang="ts">
import { Game } from "../common/types";
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      search: "",
      games: [] as Game[],
    };
  },
  methods: {
    searchGames() {
      const filter = this.search ? this.search : "";
      fetch(`api/games?filter=${filter}&amount=10`)
        .then((response) => response.json())
        .then((data) => {
          this.games = data;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
    gameSelected(game: string) {
      if (typeof game === "object" && game !== null) {
        this.$router.push(`/game/${(game as Game).game_id}`);
      }
    },
  },
  created() {
    this.searchGames();
  },
});
</script>
