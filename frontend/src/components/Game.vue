<template>
<v-card class="mx-auto" max-width="400">
    <v-img
    class="align-start text-white"
    height="400"
    src="https://image.api.playstation.com/vulcan/ap/rnd/202208/1623/Zofebh60Ue7Zt5sC10UAtU3D.png"
    cover>
    <v-card-title>{{jogo.title}}</v-card-title>
    <v-card-subtitle class='pt-0'> {{jogo.publisher}} </v-card-subtitle>
    <v-card-subtitle class='pt-0'> {{jogo.release_year}} </v-card-subtitle></v-img>
    <v-card-text>
        <v-row justify="start">
          <v-col cols="auto">
            <v-btn density="compact" color="purple">{{jogo.genre[0]}}</v-btn>
          </v-col>
          <v-col cols="auto">
            <v-btn density="compact" color="blue">{{jogo.genre[1]}}</v-btn>
          </v-col>
        </v-row>
    </v-card-text>
  
<v-card-actions>
    <v-btn color="green"> Reviews </v-btn>
</v-card-actions>
</v-card>
</template>
<script lang="ts">
import {defineComponent} from "vue";
export default defineComponent({
name: "jogo",
data(){
//Valores mockados por enquanto
// Falta usar valores do Banco de Dados
    return{
        jogo: {
            image :  'https://image.api.playstation.com/vulcan/ap/rnd/202208/1623/Zofebh60Ue7Zt5sC10UAtU3D.png',
            title : "Outer Wilds",
            publisher : "Mobius Digital",
            release_year : "2019",
            genre : ["Mistério", "Aventura"],
}}}})
</script>