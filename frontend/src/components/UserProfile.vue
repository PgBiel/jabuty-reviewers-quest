<template>
  <v-container>
    <v-card class="mx-auto" rounded="0">
      <v-col md="4" class="ma-4">
        <v-avatar color="grey" size="150" rounded="0">
          <v-icon icon="mdi-information"></v-icon>
        </v-avatar>
      </v-col>
      <v-row md="4" class="mx-4" no-gutters>
        <v-list-item class="text-black">{{ user.name }}</v-list-item>
        <v-col></v-col>
        <v-btn rounded="rounded-lg" color="red"> Logout </v-btn>
      </v-row>
      <v-row md="4" class="pl-6 my-3" no-gutters> {{ user.bio }} </v-row>
      <v-row md="4" class="pl-6 my-4 ga-2" no-gutters>
        <v-chip color="primary"> {{ user.interests }} </v-chip>
      </v-row>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "UserProfile",
  data() {
    return {
      user: {
        name: "Pepito",
        bio: "I'm flying high defying gravity",
        interests: "RPG",
      },
    };
  },
});
</script>
