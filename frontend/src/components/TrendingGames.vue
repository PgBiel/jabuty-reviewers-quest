<template>
  <v-container>
    <v-card v-for="game in games" :key="game.game_id" class="game-card">
      <v-row>
        <v-col cols="auto">
          <v-avatar size="200" rounded="0">
            <v-img :src="game.image" cover></v-img>
          </v-avatar>
        </v-col>
        <v-col cols="auto">
          <v-card-title>{{ game.name }}</v-card-title>
          <v-card-subtitle>
            <v-rating
              density="compact"
              :model-value="game.stars"
              :readonly="true"
              :half-increments="true"
            ></v-rating>
          </v-card-subtitle>
          <v-card-text>
            <v-chip :key="game.genre" class="genre-chip" outlined>
              {{ game.genre }}
            </v-chip>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { Game, StarredGame, Review } from "../common/types";
import { defineComponent } from "vue";

export default defineComponent({
  data() {
    return {
      games: [] as StarredGame[],
    };
  },
  methods: {
    async getGames() {
      const gamesResponse = await fetch("/api/trending_games");
      const games: Game[] = await gamesResponse.json();
      const starredGames: StarredGame[] = [];
      for (const game of games) {
        const reviewsResponse = await fetch(
          "/api/game/" + game.game_id + "/reviews",
        );
        const reviews: Review[] = await reviewsResponse.json();
        const totalStars = reviews
          .map((review) => review.stars)
          .reduce((previous, current) => previous + current, 0);
        const averageStars = totalStars / reviews.length;
        const starredGame: StarredGame = { stars: averageStars, ...game };
        starredGames.push(starredGame);
      }
      this.games = starredGames;
    },
  },
  created() {
    this.getGames();
  },
});
</script>

<style scoped>
.game-card {
  margin-bottom: 20px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}

.genre-chip {
  margin-right: 5px;
  margin-bottom: 5px;
}
</style>
