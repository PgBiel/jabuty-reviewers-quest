<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="6" lg="4">
        <v-card>
          <v-card-title class="headline text-center">
            Create Account
          </v-card-title>
          <v-card-text>
            <v-form ref="form" @submit.prevent="registerUser">
              <v-text-field
                v-model="user.username"
                label="Username"
                :rules="rules.usernameRules"
              ></v-text-field>
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
                :rules="rules.passwordRules"
                validate-on="submit"
              ></v-text-field>
              <v-text-field
                v-model="user.password_confirmation"
                label="Confirm Password"
                type="password"
                :rules="[passwordConfirmationRule]"
                validate-on="lazy submit"
              ></v-text-field>
              <v-btn color="indigo" type="submit" block> Sign Up </v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "RegisterUser",
  data() {
    return {
      user: {
        username: "",
        email: "",
        password: "",
        password_confirmation: "",
      },
      rules: {
        usernameRules: [(v: string) => !!v || "Username is required"],
        emailRules: [
          (v: string) => !!v || "Email is required",
          (v: string) => /.+@.+\..+/.test(v) || "Invalid e-mail.",
        ],
        passwordRules: [
          (v: string) => !!v || "Password is required",
          (v: string) =>
            (v && v.length >= 6) || "Password must have 6+ characters",
          (v: string) =>
            /(?=.*[A-Z])/.test(v) || "Must have one uppercase character",
          (v: string) => /(?=.*\d)/.test(v) || "Must have one number",
        ],
      },
    };
  },
  computed: {
    passwordConfirmationRule() {
      return () =>
        this.user.password === this.user.password_confirmation ||
        "Password must match";
    },
  },
  methods: {
    registerUser() {
      // Validate form
      const form = this.$refs.form as { isValid: () => boolean };
      if (!form.isValid) {
        return;
      }
      // Send POST request to backend
      fetch("http://localhost:5000/signup", {
        method: "POST",
        body: JSON.stringify(this.user),
      })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    },
  },
});
</script>
