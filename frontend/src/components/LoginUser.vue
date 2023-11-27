<template>
  <v-row justify="center">
    <v-col cols="12" sm="8" md="6" lg="4">
      <v-card>
        <v-card-title class="headline text-center"> Login afre </v-card-title>
        <v-card-text>
          <v-form ref="form" @submit.prevent="loginUser">
            <v-text-field
              v-model="user.email"
              label="Email"
              type="email"
              :rules="rules.emailRules"
            ></v-text-field>
            <v-text-field
              v-model="user.password"
              label="Password"
              type="password"
            ></v-text-field>
            <v-btn color="indigo" type="submit" block> Fazer Login </v-btn>
            <div>
              <router-link to="/register">Cadastro</router-link>
            </div>
          </v-form>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "LoginUser",
  data() {
    return {
      user: {
        email: "",
        password: "",
      },
      rules: {
        emailRules: [
          (v: string) => !!v || "Email is required",
          (v: string) => /.+@.+\..+/.test(v) || "Invalid e-mail.",
        ],
        passwordRules: [(v: string) => !!v || "Password is required"],
      },
    };
  },
  methods: {
    loginUser() {
      // Validate form
      const form = this.$refs.form as { isValid: () => boolean };
      if (!form.isValid) {
        return;
      }

      // Format data
      const formData = new FormData();
      formData.append("email", this.user.email);
      formData.append("password", this.user.password);

      // Send POST request to backend
      fetch("/api/user/login", {
        method: "POST",
        body: formData,
      })
        .then((response) => {
          if (response.ok) {
            alert("Login efetuado com sucesso.");
          } else {
            alert(
              "Login não pôde ser realizado. Verifique que digitou a senha correta.",
            );
          }
        })
        .catch((_error) => {
          alert(
            "Login não pôde ser realizado. Verifique que digitou a senha correta.",
          );
        });
    },
  },
});
</script>
