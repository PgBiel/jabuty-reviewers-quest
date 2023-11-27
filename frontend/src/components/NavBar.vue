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
            item-text="name"
            item-value="id"
            label="Search"
            hide-details
            clearable
            @input="searchGames"
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
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      search: "",
      // Mock data
      games: [
        "God of War",
        "The Last of Us",
        "Uncharted",
        "The Witcher",
        "Red Dead Redemption",
        "Horizon Zero Dawn",
        "Bloodborne",
        "Persona 5",
        "League of Legends",
        "Valorant",
        "Counter Strike",
        "Overwatch",
        "Undertale",
        "Outer Wilds",
        "Hollow Knight",
      ],
    };
  },
  methods: {
    searchGames() {
      console.log(this.search);
    },
  },
});
</script>
