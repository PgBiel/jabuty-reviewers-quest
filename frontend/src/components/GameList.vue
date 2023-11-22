<template>
  <v-container>
    <v-card v-for="game in games" :key="game.id" class="game-card">
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
            <v-chip
              v-for="genre in game.genres"
              :key="genre"
              class="genre-chip"
              outlined
            >
              {{ genre }}
            </v-chip>
          </v-card-text>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
interface Game {
  id: number;
  name: string;
  image: string;
  stars: number;
  genres: string[];
}
export default defineComponent({
  data() {
    return {
      games: [] as Game[],
    };
  },
  methods: {
    getGames() {
      // Mock data
      const mockData = [
        {
          id: 1,
          name: "Game 1",
          image: "https://picsum.photos/1920/1070?random",
          stars: 4.5,
          genres: ["Action", "Adventure"],
        },
        {
          id: 2,
          name: "Game 2",
          image: "https://picsum.photos/1920/1060?random",
          stars: 3.8,
          genres: ["RPG", "Strategy"],
        },
        {
          id: 3,
          name: "Game 3",
          image: "https://picsum.photos/1920/1080?random",
          stars: 5,
          genres: ["Action", "Adventure", "RPG"],
        },
      ];
      this.games = mockData;
    },
  },
  created() {
    console.log("GameList created");
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
