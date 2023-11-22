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
          <v-text-field
            v-model="search"
            placeholder="Search"
            append-inner-icon="mdi-magnify"
            hide-details
          ></v-text-field>
        </v-col>
        <v-col cols="auto" class="ml-auto">
          <v-icon>mdi-account-circle</v-icon>
        </v-col>
      </v-row>
    </v-container>
  </v-app-bar>
</template>

<script lang="ts">
export default {
  data() {
    return {
      search: "",
    };
  },
};
</script>
