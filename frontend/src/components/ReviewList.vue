<template>
  <v-col justify="start">
    <Game :game_id="$route.params.id.toString()" />
    <v-dialog v-model="review_nova.dialog" persistent width="1024">
      <template v-slot:activator="{ props }">
        <v-container class="text-center">
          <v-btn
            class="mx-auto"
            color="black"
            v-bind="props"
            @click="verificaLogin()"
          >
            Escrever Review
          </v-btn>
        </v-container>
      </template>
      <v-card>
        <v-rating v-model="review_nova.rating">
          <template v-slot:item="props">
            <v-icon
              :color="props.isFilled ? 'black' : 'grey lighten-1'"
              @click="TrocaRating(props)"
              >mdi-star
            </v-icon>
          </template>
        </v-rating>
        <v-card-title>
          <span class="text-h5">Review</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="30" sm="10" md="30">
                <v-text-field
                  v-model="review_nova.text"
                  label=""
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="black"
            variant="text"
            @click="review_nova.dialog = false"
          >
            Voltar
          </v-btn>
          <v-btn color="black" variant="text" @click="writeReview()">
            Salvar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-col>
  <v-container>
    <v-card
      v-for="review in reviews"
      :key="review.review_id"
      class="mx-auto"
      max-width="500"
    >
      <v-row>
        <v-col cols="auto">
          <v-img class="align-start text-black" height="200">
            <v-avatar color="grey">
              <v-icon icon="mdi-account-circle"></v-icon>
            </v-avatar>
            <v-card-text>{{ review.author_name }}</v-card-text>

            <v-rating v-model="review.stars"></v-rating>
            <v-card-text>{{ review.body }} </v-card-text>
          </v-img>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script lang="ts">
import { JSXComponent } from "vue";
import { NamedReview } from "../common/types";
import { defineComponent } from "vue";
import Game from "./Game.vue";
export default defineComponent({
  data() {
    return {
      reviews: [] as NamedReview[],
      review_nova: {
        dialog: false,
        rating: 0,
        text: "",
      },
    };
  },
  methods: {
    TrocaRating(props: {
      value?: number;
      index: number;
      isFilled?: boolean;
      isHovered?: boolean;
      icon?:
        | string
        | (string | [path: string, opacity: number])[]
        | JSXComponent;
      color?: string | undefined;
      props?: Record<string, unknown>;
      rating?: number;
    }) {
      console.log(props.index + 1);
      this.review_nova.rating = props.index + 1;
    },
    async getReviews() {
      const reviewsResponse = await fetch(
        "/api/game/" + this.$route.params.id + "/reviews",
      );
      const reviews: NamedReview[] = await reviewsResponse.json();
      this.reviews = reviews;
    },
    writeReview() {
      const formData = new FormData();
      formData.append("body", this.review_nova.text);
      // Valor de stars passado como str, deve ser convertido
      formData.append("stars", this.review_nova.rating.toString());
      fetch("/api/game/" + this.$route.params.id + "/reviews", {
        method: "POST",
        body: formData,
      })
        .then((_response) => {
          if (_response.status === 401) {
            // usuário não está logado
            this.$router.push({ name: "login" });
          } else {
            this.review_nova.dialog = false;
            this.getReviews();
            alert("Review adicionada!");
          }
        })
        .catch((_error) => {
          alert("Não foi possível adicionar sua review. Tente novamente.");
        });
    },
    verificaLogin() {
      fetch("/api/user/self").then((_response) => {
        if (_response.status === 401) {
          // usuário não está logado
          this.$router.push({ name: "login" });
        }
      });
    },
  },
  created() {
    this.getReviews();
  },
  components: { Game },
});
</script>
