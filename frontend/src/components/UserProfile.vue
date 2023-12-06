<template>
  <v-container v-if="user">
    <v-card class="mx-auto" rounded="0">
      <v-col md="4" class="ma-4">
        <v-avatar color="grey" size="150" rounded="0">
          <v-icon icon="mdi-information"></v-icon>
        </v-avatar>
      </v-col>
      <v-row md="4" class="mx-4" no-gutters>
        <v-list-item class="text-weight-bold">{{ user.name }}</v-list-item>
        <v-col></v-col>
        <v-btn @click="logout" rounded="rounded-lg" color="red"> Logout </v-btn>
      </v-row>
      <v-row md="4" class="pl-6 my-3" no-gutters>
        {{ user.bio || "Nenhuma bio" }}
      </v-row>
      <v-row md="4" class="pl-6 my-4 ga-2" no-gutters>
        <v-chip color="primary">
          {{ user.interests || "Nenhum interesse" }}
        </v-chip>
      </v-row>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
interface User {
  user_id: number;
  name: string;
  bio: string;
  interests: string;
  reviews: string;
}

export default defineComponent({
  name: "UserProfile",
  data() {
    return {
      user: null as User | null,
    };
  },
  methods: {
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
    logout() {
      fetch("/api/user/logout")
        .then((_response) => {
          alert("Logout efetuado com sucesso");
          this.$router.push("/");
        })
        .catch((_error) => {
          alert("Erro ao efetuar logout");
        });
    },
  },
  created() {
    this.getCurrentUser();
  },
});
</script>
