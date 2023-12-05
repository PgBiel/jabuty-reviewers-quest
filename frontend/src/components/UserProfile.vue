<template>
  <v-container>
    <v-card class="mx-auto" rounded="0">
      <v-col md="4" class="ml-auto">
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
        <v-chip color="primary"> {{ user.interesses[0] }} </v-chip>
        <v-chip color="primary"> {{ user.interesses[1] }} </v-chip>
        <v-chip color="primary"> {{ user.interesses[2] }} </v-chip>
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
        interesses: ["RPG", "Aventura", "Ação"],
      },
    };
  },
});
</script>
