<template>
  <v-container>
    <v-col> </v-col>
    <v-card
      v-for="review in reviews"
      :key="review.review_id"
      class="mx-auto"
      max-width="500"
    >
      <v-img class="align-start text-black" height="200">
        <v-row align="end" class="spacer" no-gutters>
          <v-avatar color="grey">
            <v-icon icon="mdi-account-circle"></v-icon>
          </v-avatar>
        </v-row>
        <v-rating v-model="review.stars"></v-rating>
        <v-card-text>{{ review.body }} </v-card-text>
      </v-img>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Review } from "../common/types";
import { defineComponent } from "vue";
export default defineComponent({
  data() {
    return {
      reviews: [] as Review[],
    };
  },
  methods: {
    async getReviews() {
      // Essa parte acho q está errada, tenho que extrair o game_id da URL
      const gameResponse = await fetch("/api/game");
      const game = await gameResponse.json();
      const reviewsResponse = await fetch(
        "/api/game/" + game.game_id + "/reviews",
      );
      const reviews: Review[] = await reviewsResponse.json();
      this.reviews = reviews;
    },
    created() {
      this.getReviews();
    },
  },
});
</script>
