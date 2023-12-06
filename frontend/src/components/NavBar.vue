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
        <v-col cols="auto">
          <v-menu v-if="user">
            <template v-slot:activator="{ props }">
              <v-btn v-bind="props" icon>
                <v-icon>mdi-account-circle</v-icon>
              </v-btn>
            </template>
            <v-list>
              <v-list-item>
                <v-list-item-title class="text-center">
                  {{ user.name }}
                </v-list-item-title>
              </v-list-item>
              <v-list-item>
                <v-btn
                  :to="{ name: 'profile', params: { userId: user.user_id } }"
                  elevation="0"
                >
                  Profile
                </v-btn>
              </v-list-item>
              <v-list-item>
                <v-btn elevation="0">Logout</v-btn>
              </v-list-item>
            </v-list>
          </v-menu>
          <v-btn v-else to="/login" variant="outlined">Login</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script lang="ts">
import { Game } from "../common/types";
import { defineComponent } from "vue";
interface User {
  user_id: number;
  name: string;
  bio: string;
  interests: string;
  reviews: string;
}
export default defineComponent({
  data() {
    return {
      search: "",
      games: [] as Game[],
      user: null as User | null,
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
    gameSelected(game: string | Game) {
      if (typeof game === "object" && game !== null) {
        this.$router.push(`/game/${(game as Game).game_id}`);
      }
    },
    getCurrentUser() {
      fetch("/api/user/self")
        .then((response) => {
          if (response.status === 401) {
            return null;
          } else {
            return response.json();
          }
        })
        .then((data) => {
          this.user = data as User;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
  created() {
    this.searchGames();
    this.getCurrentUser();
  },
});
</script>
