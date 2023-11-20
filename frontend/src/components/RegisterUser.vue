<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6">
        <v-card>
          <v-card-title class="headline">Cadastro de Usuário</v-card-title>
          <v-card-text>
            <v-form @submit.prevent>
              <v-text-field
                v-model="user.name"
                label="Name"
                required
              ></v-text-field>
              <v-text-field
                v-model="user.email"
                label="Email"
                type="email"
                required
              ></v-text-field>
              <v-text-field
                v-model="user.password"
                label="Password"
                type="password"
                required
              ></v-text-field>
              <v-btn type="submit">Cadastrar</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>
<script lang="ts">
export default {
  data() {
    return {
      user: {
        name: "",
        email: "",
        password: "",
      },
    };
  },
  methods: {},
};
</script>
