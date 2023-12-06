<template>
  <v-card class="mx-auto" max-width="400">
    <v-img class="align-start text-white" height="400" :src="jogo.image" cover>
      <v-card-title>{{ jogo.name }}</v-card-title>
      <v-card-subtitle class="pt-0"> {{ jogo.publisher }} </v-card-subtitle>
      <v-card-subtitle class="pt-0">
        {{ jogo.release_year }}
      </v-card-subtitle></v-img
    >
    <v-card-text>
      <v-row justify="start">
        <v-col cols="auto">
          <v-btn density="compact" color="purple">{{ jogo.genre }}</v-btn>
        </v-col>
      </v-row>
    </v-card-text>
  </v-card>
</template>
<script lang="ts">
import { Game } from "@/common/types";
import { defineComponent } from "vue";
export default defineComponent({
  name: "GameCard",
  props: {
    game_id: { type: String, required: true },
  },
  data() {
    //Valores mockados por enquanto
    // Falta usar valores do Banco de Dados
    return {
      jogo: {
        name: "",
        image: "",
        publisher: "",
        release_year: 0,
        genre: "",
      },
    };
  },
  methods: {
    async loadGame() {
      const response = await fetch("/api/game/" + this.game_id);
      if (!response.ok) {
        return;
      }
      const game: Game = await response.json();
      this.jogo.name = game.name;
      this.jogo.image = game.image;
      this.jogo.publisher = game.publisher;
      this.jogo.release_year = game.release_year;
      this.jogo.genre = game.genre;
    },
  },
  created() {
    this.loadGame();
  },
});
</script>
