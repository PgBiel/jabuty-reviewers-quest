<template>
  <v-card class="mx-auto" max-width="500">
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
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "ReviewCard",
  data() {
    // Valores mockados por enquanto
    return {
      review: {
        iniciais: "L",
        title: "Titulo",
        rating: 4,
        text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod",
      },
    };
  },
});
</script>
