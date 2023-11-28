<template>
  <v-container align="center" justify="center" fill-height>
    <v-row justify="space-around">
      <v-col>
        <v-card width="400" color="green">
          <v-img height="200px" src="">
            <v-app-bar class="mt-8" color="rgba(255,255,255,0)" text>
            </v-app-bar>

            <v-avatar size="100">
              <img
                src="<img src=https://drive.google.com/uc?id=1Hqu-piDnaGiQINi8cT0glG-bOUvKwYgm"
                alt="User image"
              />"
            </v-avatar>

            <v-spacer></v-spacer>
          </v-img>

          <v-card-text>
            <v-row justify="start">
              <v-col cols="auto">
                <v-btn density="compact" color="purple">{{
                  user.interesses[0]
                }}</v-btn>
              </v-col>
              <v-col cols="auto">
                <v-btn density="compact" color="blue">{{
                  user.interesses[1]
                }}</v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  name: "UserProfile",
  data() {
    return {
      user: {
        image:
          "https://drive.google.com/uc?id=1Hqu-piDnaGiQINi8cT0glG-bOUvKwYgm",
        name: "Pepito",
        bio: "I'm flying high defying gravity",
        interesses: ["RPG", "Aventura"],
      },
    };
  },
});
</script>
