<template>
  <v-container>
    <v-col> </v-col>
    <v-card
      v-for="review in reviews"
      :key="review.title"
      class="mx-auto"
      max-width="500"
    >
      <v-img class="align-start text-black" height="200">
        <v-row align="end" class="spacer" no-gutters>
          <v-avatar color="purple">
            <span class="text-h5">{{ review.iniciais }}</span>
          </v-avatar>
          <v-card-title>{{ review.title }}</v-card-title>
        </v-row>
        <v-rating v-model="review.rating"></v-rating>
        <v-card-text>{{ review.text }} </v-card-text>
      </v-img>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "ReviewCard",
  data() {
    // Valores mockados por enquanto
    return {
      reviews: [
        {
          iniciais: "L",
          title: "Titulo",
          rating: 4,
          text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod",
        },
        {
          iniciais: "T",
          title: "Titulo 2",
          rating: 4,
          text: " consectetur adipiscing elit, sed do eiusmod",
        },
      ],
    };
  },
});
</script>
