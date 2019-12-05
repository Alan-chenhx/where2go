<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="600">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>
      </template>

      <v-card fluid>
        <v-img :src="attr.background" height="200px" class="white--text text-center align-end"></v-img>
        <v-card-title class="headline">{{ attr.name }}</v-card-title>
        <v-card-subtitle>{{ attr.address }}</v-card-subtitle>
        <v-card-text>
          <v-row align="center" class="mx-0">
            <v-rating
              :value="attr.rating"
              color="amber"
              dense
              half-increments
              readonly
              size="14"
              v-if="!!attr.rating"
            ></v-rating>
            <div class="grey--text ml-4" v-if="!!attr.rating">{{attr.rating}}</div>
          </v-row>
          <div class="mb-1 black--text">{{ attr.price }} • {{ attr.tag }}</div>
          {{ attr.discription }}
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      attr: {
        name: "Bradbury Building",
        background:
          "https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg",
        discription:
          "Head downtown to see Bradbury Building and star in your own film noir. Originally designed by Sumner Hunt, Bradbury Building has been standing tall since 1893 when a millionaire businessman Lewis L. Bradbury commissioned it from George Wyman. Added to the list of the Los Angeles Cultural Heritage Commission, the building played a starring role in many music videos of artists like Janet Jackson and Genesis, as well as various films. Take a stroll through the structure to admire the Romanesque style that rules the decor--including an interior central court--or ride the open-cage elevators for a unique experience. Use Inspirock's suggestions to plan your Los Angeles trip and find the best activities and attractions for your vacation.",
        rating: 4.5,
        tag: "Architectural Building",
        address: "304 S Broadway, Los Angeles, CA 90013, USA",
        price: "$"
      }
    };
  }
};
</script>
