<template>
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="800">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>
      </template>

      <v-card>
        <div class="pt-5">
          <core-search style="width:70%;postion:center;margin-left: auto;margin-right: auto;" />
        </div>
        <v-row class="pt-5">
          <v-img
            :src="item.background"
            max-height="200"
            max-width="300"
            class="white--text text-center ml-12"
          ></v-img>

          <v-col>
            <v-card-title>{{ item.name }}</v-card-title>
            <v-card-subtitle>{{ item.address }}</v-card-subtitle>
            <v-card-text>
              <v-row align="center" class="mx-0">
                <v-rating
                  :value="item.rating"
                  color="amber"
                  dense
                  half-increments
                  readonly
                  size="14"
                  v-if="!!item.rating"
                ></v-rating>
                <div class="grey--text ml-4" v-if="!!item.rating">{{item.rating}}</div>
              </v-row>
              <div class="mb-1 black--text">{{ item.price }} • {{ item.tag }}</div>
              <div style="display: -webkit-box;-webkit-line-clamp: 3; -webkit-box-orient: vertical;overflow: hidden;">{{ item.discription }}</div>
              <!-- <div class="d-block text-truncate" style="max-height=400px">{{ item.discription }}</div> -->
            </v-card-text>
          </v-col>
        </v-row>
        <v-divider></v-divider>
        <v-row class="pt-12">
          <v-textarea
              class=" mx-12"
              style="max-width:300px"
              v-model="item.duration"
              rowHeight=24
              auto-grow=true
              clearable=true
              :counter="counter ? counter : false"
              label="Duration"
              outlined=true
            ></v-textarea>
            <div class="mt-12 text-center">
              Value: {{ item.duration }}
            </div>
            <v-spacer></v-spacer>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="dialog = false">OK</v-btn>
          </v-card-actions>
        </v-row>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
export default {
  data() {
    return {
      dialog: false,
      item: {
        name: "Bradbury Building",
        background:
          "https://s.inspirockcdn.com/ds10/photos/United States/1/bradbury-building--1985987038.jpg",
        discription:
          "Head downtown to see Bradbury Building and star in your own film noir. Originally designed by Sumner Hunt, Bradbury Building has been standing tall since 1893 when a millionaire businessman Lewis L. Bradbury commissioned it from George Wyman. Added to the list of the Los Angeles Cultural Heritage Commission, the building played a starring role in many music videos of artists like Janet Jackson and Genesis, as well as various films. Take a stroll through the structure to admire the Romanesque style that rules the decor--including an interior central court--or ride the open-cage elevators for a unique experience. Use Inspirock's suggestions to plan your Los Angeles trip and find the best activities and attractions for your vacation.",
        rating: 4.5,
        tag: "Architectural Building",
        address: "304 S Broadway, Los Angeles, CA 90013, USA",
        price: "$",
        duration:30
      }
    };
  }
};
</script>
